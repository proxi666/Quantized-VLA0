#!/usr/bin/env python3
"""Schedule a full multi-GPU VLA-0 LIBERO quantization benchmark."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from benchmark_config import (
    DEFAULT_ACTION_HORIZON,
    DEFAULT_ENSEMBLE_PREDICTION,
    DEFAULT_MODES,
    DEFAULT_SEED,
    DEFAULT_SUITES,
    DEFAULT_TASK_ID_COUNT,
    discover_tasks,
    expected_episode_count,
    safe_name,
)


SCRIPT_DIR = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vla0-root", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--gpus", default="0,1,2,3")
    parser.add_argument("--modes", nargs="+", default=DEFAULT_MODES)
    parser.add_argument("--suites", nargs="+", default=DEFAULT_SUITES)
    parser.add_argument("--task-id-count", type=int, default=DEFAULT_TASK_ID_COUNT)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--action-horizon", type=int, default=DEFAULT_ACTION_HORIZON)
    parser.add_argument("--ensemble-prediction", type=int, default=DEFAULT_ENSEMBLE_PREDICTION)
    parser.add_argument("--ensemble-version", type=int, default=1)
    parser.add_argument("--ensemble-2-weight", type=float, default=0.5)
    parser.add_argument("--generate-temperature", type=float, default=0.0)
    parser.add_argument("--num-steps", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--smoke", action="store_true", help="Run one shard per GPU only.")
    parser.add_argument("--dry-run", action="store_true", help="Write manifest but do not launch workers.")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def parse_gpus(value: str) -> list[str]:
    gpus = [item.strip() for item in value.split(",") if item.strip()]
    if not gpus:
        raise ValueError("--gpus must contain at least one GPU id")
    return gpus


def shard_output_dir(output_root: Path, job: dict[str, Any]) -> Path:
    return (
        output_root
        / "runs"
        / job["mode"]
        / job["suite"]
        / safe_name(job["task_name"])
        / f"shard_{job['task_id_index']:02d}_of_{job['task_id_count']:02d}"
    )


def build_manifest(args: argparse.Namespace, output_root: Path, gpus: list[str]) -> list[dict[str, Any]]:
    vla0_root = Path(args.vla0_root).expanduser().resolve()
    checkpoint = Path(args.checkpoint).expanduser().resolve()
    tasks_by_suite = discover_tasks(vla0_root, args.suites)
    episodes_per_shard = expected_episode_count(args.task_id_count)

    jobs = []
    job_index = 0
    for mode in args.modes:
        for suite in args.suites:
            for task_name in tasks_by_suite[suite]:
                for task_id_index in range(args.task_id_count):
                    gpu_id = gpus[job_index % len(gpus)]
                    job = {
                        "job_id": f"{job_index:06d}",
                        "created_at": now_iso(),
                        "vla0_root": str(vla0_root),
                        "checkpoint": str(checkpoint),
                        "mode": mode,
                        "suite": suite,
                        "task_name": task_name,
                        "task_id_index": task_id_index,
                        "task_id_count": args.task_id_count,
                        "episodes_per_shard": episodes_per_shard,
                        "gpu_id": gpu_id,
                        "seed": args.seed,
                        "action_horizon": args.action_horizon,
                        "ensemble_prediction": args.ensemble_prediction,
                        "ensemble_version": args.ensemble_version,
                        "ensemble_2_weight": args.ensemble_2_weight,
                        "generate_temperature": args.generate_temperature,
                        "num_steps": args.num_steps,
                        "amp": False,
                        "resume": args.resume,
                    }
                    out_dir = shard_output_dir(output_root, job)
                    job["output_dir"] = str(out_dir)
                    job["results_json_path"] = str(out_dir / "results.json")
                    job["status_path"] = str(out_dir / "status.json")
                    jobs.append(job)
                    job_index += 1

    if args.smoke:
        jobs = jobs[: len(gpus)]
        for index, job in enumerate(jobs):
            job["gpu_id"] = gpus[index % len(gpus)]
    return jobs


def split_jobs_by_gpu(jobs: list[dict[str, Any]], gpus: list[str]) -> dict[str, list[dict[str, Any]]]:
    by_gpu = {gpu: [] for gpu in gpus}
    for job in jobs:
        by_gpu[str(job["gpu_id"])].append(job)
    return by_gpu


def worker_env(gpu_id: str) -> dict[str, str]:
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = gpu_id
    env["MUJOCO_GL"] = "egl"
    env["PYOPENGL_PLATFORM"] = "egl"
    env["MUJOCO_EGL_DEVICE_ID"] = "0"
    env.setdefault("TOKENIZERS_PARALLELISM", "false")
    return env


def launch_workers(args: argparse.Namespace, output_root: Path, jobs: list[dict[str, Any]], gpus: list[str]) -> int:
    by_gpu = split_jobs_by_gpu(jobs, gpus)
    worker_root = output_root / "worker_jobs"
    log_root = output_root / "logs"
    worker_root.mkdir(parents=True, exist_ok=True)
    log_root.mkdir(parents=True, exist_ok=True)

    processes = []
    for gpu_id in gpus:
        gpu_jobs = by_gpu[gpu_id]
        if not gpu_jobs:
            continue
        jobs_path = worker_root / f"gpu_{gpu_id}.json"
        write_json(jobs_path, gpu_jobs)
        log_path = log_root / f"worker_gpu_{gpu_id}.log"
        cmd = [
            sys.executable,
            "-u",
            str(SCRIPT_DIR / "worker_libero.py"),
            "--jobs-json",
            str(jobs_path),
            "--vla0-root",
            str(Path(args.vla0_root).expanduser().resolve()),
            "--checkpoint",
            str(Path(args.checkpoint).expanduser().resolve()),
            "--gpu-id",
            gpu_id,
        ]
        if args.resume:
            cmd.append("--resume")
        log_file = log_path.open("w", encoding="utf-8")
        print(f"[scheduler] launching gpu={gpu_id} jobs={len(gpu_jobs)} log={log_path}", flush=True)
        proc = subprocess.Popen(
            cmd,
            cwd=str(Path(args.vla0_root).expanduser().resolve()),
            env=worker_env(gpu_id),
            stdout=log_file,
            stderr=subprocess.STDOUT,
        )
        processes.append((gpu_id, proc, log_file))

    failures = 0
    while processes:
        alive = []
        for gpu_id, proc, log_file in processes:
            rc = proc.poll()
            if rc is None:
                alive.append((gpu_id, proc, log_file))
                continue
            log_file.close()
            print(f"[scheduler] worker gpu={gpu_id} finished rc={rc}", flush=True)
            if rc != 0:
                failures += 1
        processes = alive
        if processes:
            time.sleep(30)
    return failures


def main() -> int:
    args = parse_args()
    output_root = Path(args.output_root).expanduser().resolve()
    gpus = parse_gpus(args.gpus)

    if not shutil.which("nvidia-smi"):
        print("[scheduler] warning: nvidia-smi not found; continuing anyway", flush=True)

    output_root.mkdir(parents=True, exist_ok=True)
    jobs = build_manifest(args, output_root, gpus)
    manifest = {
        "created_at": now_iso(),
        "vla0_root": str(Path(args.vla0_root).expanduser().resolve()),
        "checkpoint": str(Path(args.checkpoint).expanduser().resolve()),
        "output_root": str(output_root),
        "gpus": gpus,
        "modes": args.modes,
        "suites": args.suites,
        "task_id_count": args.task_id_count,
        "episodes_per_shard": expected_episode_count(args.task_id_count),
        "expected_rollouts": len(jobs) * expected_episode_count(args.task_id_count),
        "jobs": jobs,
    }
    write_json(output_root / "manifest.json", manifest)
    print(
        f"[scheduler] wrote manifest jobs={len(jobs)} "
        f"expected_rollouts={manifest['expected_rollouts']} output={output_root}",
        flush=True,
    )

    if args.dry_run:
        return 0

    failures = launch_workers(args, output_root, jobs, gpus)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
