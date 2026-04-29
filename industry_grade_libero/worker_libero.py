#!/usr/bin/env python3
"""Single-GPU worker for industry-grade VLA-0 LIBERO evaluation."""

from __future__ import annotations

import argparse
import gc
import json
import os
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any

import torch

from benchmark_config import add_vla0_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs-json", required=True)
    parser.add_argument("--vla0-root", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--gpu-id", required=True)
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def is_complete(job: dict[str, Any]) -> bool:
    status_path = Path(job["status_path"])
    if not status_path.exists():
        return False
    try:
        status = read_json(status_path)
    except Exception:
        return False
    return status.get("status") == "success" and Path(job["results_json_path"]).exists()


def build_model_act(model: Any, device: str, enable_amp: bool, generate_temperature: float):
    device_type = "cuda" if str(device).startswith("cuda") else "cpu"

    def model_act(*args: Any, **kwargs: Any) -> Any:
        with torch.no_grad():
            with torch.autocast(
                device_type=device_type, dtype=torch.bfloat16, enabled=enable_amp
            ):
                return model(
                    *args,
                    **kwargs,
                    generate_temperature=generate_temperature,
                    get_loss=False,
                    get_action=True,
                )

    return model_act


def load_mode_model(vla0_root: Path, checkpoint: str, mode: str, device: str):
    add_vla0_paths(vla0_root)
    from rv_train.train import get_pretrained_model

    model, cfg = get_pretrained_model(
        checkpoint,
        device,
        torch_compile=False,
        load_mode=mode,
    )
    model.eval()
    return model, cfg


def run_job(job: dict[str, Any], model: Any, cfg: Any, device: str) -> dict[str, Any]:
    add_vla0_paths(Path(job["vla0_root"]))
    from roboverse.evals.libero.eval import eval as libero_eval

    started_at = time.time()
    status = {
        "job_id": job["job_id"],
        "mode": job["mode"],
        "suite": job["suite"],
        "task_name": job["task_name"],
        "task_id_index": job["task_id_index"],
        "task_id_count": job["task_id_count"],
        "gpu_id": job["gpu_id"],
        "status": "running",
        "started_at": now_iso(),
        "output_dir": job["output_dir"],
        "results_json_path": job["results_json_path"],
    }
    write_json(Path(job["status_path"]), status)

    action_type = {"qwen": cfg.MODEL.QWEN.action_type}[cfg.EXP.MODEL]
    model_act = build_model_act(
        model,
        device=device,
        enable_amp=job["amp"],
        generate_temperature=job["generate_temperature"],
    )

    try:
        Path(job["output_dir"]).mkdir(parents=True, exist_ok=True)
        libero_eval(
            model=model_act,
            action_type=action_type,
            cfg_path=cfg.DATALOADER.ROBOVERSE.cfg_path,
            cfg_opts=cfg.DATALOADER.ROBOVERSE.cfg_opts,
            task_name=job["task_name"],
            task_suite_name=job["suite"],
            log_dir=job["output_dir"],
            save_video=True,
            seed=job["seed"],
            action_horizon=job["action_horizon"],
            skip_evaluated=job["resume"],
            save_all_data=False,
            ensemble_prediction=job["ensemble_prediction"],
            ensemble_2_weight=job["ensemble_2_weight"],
            ensemble_version=job["ensemble_version"],
            task_id_index=job["task_id_index"],
            task_id_count=job["task_id_count"],
            num_steps=job["num_steps"],
        )
        result = read_json(Path(job["results_json_path"]))
        status.update(
            {
                "status": "success",
                "ended_at": now_iso(),
                "elapsed_seconds": time.time() - started_at,
                "success": result.get("success"),
                "failure": result.get("failure"),
            }
        )
    except Exception as exc:
        status.update(
            {
                "status": "failed",
                "ended_at": now_iso(),
                "elapsed_seconds": time.time() - started_at,
                "error_type": type(exc).__name__,
                "error": str(exc),
                "traceback": traceback.format_exc(),
            }
        )
    finally:
        write_json(Path(job["status_path"]), status)
    return status


def main() -> int:
    args = parse_args()
    vla0_root = Path(args.vla0_root).expanduser().resolve()
    jobs = read_json(Path(args.jobs_json))
    device = "cuda:0"

    print(
        f"[worker gpu={args.gpu_id}] starting with {len(jobs)} jobs | "
        f"visible={os.environ.get('CUDA_VISIBLE_DEVICES')}",
        flush=True,
    )
    if torch.cuda.is_available():
        torch.cuda.set_device(0)
        print(f"[worker gpu={args.gpu_id}] device={torch.cuda.get_device_name(0)}", flush=True)

    failures = 0
    modes = []
    for job in jobs:
        if job["mode"] not in modes:
            modes.append(job["mode"])

    for mode in modes:
        mode_jobs = [job for job in jobs if job["mode"] == mode]
        pending = [
            job for job in mode_jobs if not (args.resume and is_complete(job))
        ]
        if not pending:
            print(f"[worker gpu={args.gpu_id}] mode={mode} already complete", flush=True)
            continue

        print(
            f"[worker gpu={args.gpu_id}] loading mode={mode} for {len(pending)} jobs",
            flush=True,
        )
        model = None
        cfg = None
        try:
            model, cfg = load_mode_model(vla0_root, args.checkpoint, mode, device)
            for index, job in enumerate(pending, start=1):
                print(
                    f"[worker gpu={args.gpu_id}] {mode} job {index}/{len(pending)} "
                    f"{job['suite']}::{job['task_name']} shard={job['task_id_index']}",
                    flush=True,
                )
                status = run_job(job, model, cfg, device)
                if status["status"] != "success":
                    failures += 1
                    print(
                        f"[worker gpu={args.gpu_id}] failed job={job['job_id']} "
                        f"error={status.get('error')}",
                        flush=True,
                    )
        except Exception as exc:
            failures += len(pending)
            for job in pending:
                write_json(
                    Path(job["status_path"]),
                    {
                        "job_id": job["job_id"],
                        "mode": job["mode"],
                        "suite": job["suite"],
                        "task_name": job["task_name"],
                        "task_id_index": job["task_id_index"],
                        "task_id_count": job["task_id_count"],
                        "gpu_id": job["gpu_id"],
                        "status": "failed",
                        "started_at": now_iso(),
                        "ended_at": now_iso(),
                        "output_dir": job["output_dir"],
                        "results_json_path": job["results_json_path"],
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "traceback": traceback.format_exc(),
                    },
                )
            print(f"[worker gpu={args.gpu_id}] mode={mode} load failed: {exc}", flush=True)
        finally:
            del model
            del cfg
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

    print(f"[worker gpu={args.gpu_id}] finished failures={failures}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

