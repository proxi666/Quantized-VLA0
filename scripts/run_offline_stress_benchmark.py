#!/usr/bin/env python3
"""Run the released Quantized-VLA0 offline stress benchmark.

This wrapper expects a separate local checkout of the original VLA-0 codebase.
It reproduces the stratified offline benchmark used in the paper by calling
that checkout's `scripts/compare_vla0_generation_batch.py`.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


DEFAULT_RESULTS_DIR = Path(__file__).resolve().parents[1] / "results" / "generated-offline"
DEFAULT_RAW_DIR = DEFAULT_RESULTS_DIR / "raw"
DEFAULT_REPORTS_DIR = DEFAULT_RESULTS_DIR / "reports"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a stratified offline stress benchmark for VLA-0 quantization."
    )
    parser.add_argument(
        "--vla0-root",
        type=str,
        required=True,
        help="Path to a local VLA-0 checkout containing scripts/compare_vla0_generation_batch.py.",
    )
    parser.add_argument("--checkpoint", type=str, required=True)
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--split", type=str, default="train")
    parser.add_argument("--lerobot-repo-id", type=str, default="lerobot/libero_10")
    parser.add_argument(
        "--load-modes",
        nargs="+",
        default=["bf16", "int8", "nf4"],
        choices=["bf16", "int8", "nf4"],
    )
    parser.add_argument(
        "--num-strata",
        type=int,
        default=6,
        help="How many dataset strata to sample across.",
    )
    parser.add_argument(
        "--samples-per-stratum",
        type=int,
        default=24,
        help="RTX 3070-safe default is 24. Use 30 for the aggressive workshop run.",
    )
    parser.add_argument(
        "--progress-every",
        type=int,
        default=8,
        help="Forwarded to compare_vla0_generation_batch.py for per-sample progress.",
    )
    parser.add_argument(
        "--heartbeat-seconds",
        type=float,
        default=30.0,
        help="Parent-process heartbeat while each stratum subprocess is running.",
    )
    parser.add_argument(
        "--worst-k",
        type=int,
        default=10,
        help="How many worst-drift samples to keep per quantized mode.",
    )
    parser.add_argument(
        "--results-dir",
        type=str,
        default=str(DEFAULT_RESULTS_DIR),
    )
    parser.add_argument(
        "--stream-subprocess",
        action="store_true",
        help="Stream the child process output directly instead of heartbeat mode.",
    )
    return parser.parse_args()


def format_duration(seconds: float) -> str:
    seconds = max(0.0, seconds)
    minutes, secs = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:d}h{minutes:02d}m{secs:02d}s"
    if minutes:
        return f"{minutes:d}m{secs:02d}s"
    return f"{secs:d}s"


def last_nonempty_line(log_path: Path) -> str:
    if not log_path.exists():
        return "(no log yet)"
    text = log_path.read_text(errors="ignore")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[-1] if lines else "(log empty)"


def get_dataset_length(vla0_root: Path, checkpoint: str, split: str, lerobot_repo_id: str) -> int:
    sys.path.insert(0, str(vla0_root))
    sys.path.insert(0, str(vla0_root / "scripts"))

    from compare_vla0_generation import override_lerobot_settings
    from rv_train.train import get_cfg, get_dataloader

    old_cwd = Path.cwd()
    try:
        os.chdir(vla0_root)
        cfg = get_cfg(str(Path(checkpoint).parent / "config.yaml"), "")
        cfg = override_lerobot_settings(cfg, lerobot_repo_id)
        dataset = get_dataloader(split=split, cfg=cfg, get_dataset=True)
        return len(dataset)
    finally:
        os.chdir(old_cwd)


def build_strata(
    *,
    dataset_len: int,
    num_strata: int,
    samples_per_stratum: int,
) -> list[dict[str, Any]]:
    if dataset_len <= 0:
        raise ValueError(f"Invalid dataset_len: {dataset_len}")
    if samples_per_stratum <= 0:
        raise ValueError(f"Invalid samples_per_stratum: {samples_per_stratum}")
    if samples_per_stratum > dataset_len:
        raise ValueError(
            f"samples_per_stratum={samples_per_stratum} exceeds dataset_len={dataset_len}"
        )
    if num_strata <= 0:
        raise ValueError(f"Invalid num_strata: {num_strata}")

    if num_strata == 1:
        ratios = [0.0]
    else:
        ratios = [i / (num_strata - 1) for i in range(num_strata)]

    max_start = max(0, dataset_len - samples_per_stratum)
    starts = []
    for ratio in ratios:
        starts.append(min(max_start, int(round(max_start * ratio))))

    adjusted = []
    previous_end = -1
    for start in starts:
        start = max(start, previous_end + 1)
        start = min(start, max_start)
        adjusted.append(start)
        previous_end = start + samples_per_stratum - 1

    for idx in range(len(adjusted) - 2, -1, -1):
        if adjusted[idx] + samples_per_stratum - 1 >= adjusted[idx + 1]:
            adjusted[idx] = max(0, adjusted[idx + 1] - samples_per_stratum)

    strata = []
    for idx, start in enumerate(adjusted):
        end = start + samples_per_stratum - 1
        center_ratio = 0.0 if max_start == 0 else start / max_start
        label = f"s{idx + 1:02d}_{int(round(center_ratio * 100)):02d}pct"
        strata.append(
            {
                "label": label,
                "start_index": start,
                "end_index": end,
                "num_samples": samples_per_stratum,
            }
        )

    return strata


def run_stratum(
    *,
    stratum: dict[str, Any],
    vla0_root: Path,
    compare_batch_script: Path,
    checkpoint: str,
    device: str,
    split: str,
    load_modes: list[str],
    progress_every: int,
    lerobot_repo_id: str,
    raw_dir: Path,
    heartbeat_seconds: float,
    stream_subprocess: bool,
) -> dict[str, Any]:
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    modes_tag = "_".join(load_modes)
    output_json = raw_dir / (
        f"offline_stress_{stratum['label']}_{modes_tag}_"
        f"{stratum['num_samples']}samples_{timestamp}.json"
    )
    log_path = raw_dir / (
        f"offline_stress_{stratum['label']}_{modes_tag}_"
        f"{stratum['num_samples']}samples_{timestamp}.log"
    )
    cmd = [
        sys.executable,
        "-u",
        str(compare_batch_script),
        "--checkpoint",
        checkpoint,
        "--device",
        device,
        "--split",
        split,
        "--start-index",
        str(stratum["start_index"]),
        "--num-samples",
        str(stratum["num_samples"]),
        "--progress-every",
        str(progress_every),
        "--load-modes",
        *load_modes,
        "--output-json",
        str(output_json),
        "--lerobot-repo-id",
        lerobot_repo_id,
    ]

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
    env["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

    print(
        f"[offline-stress] starting {stratum['label']} "
        f"({stratum['start_index']}..{stratum['end_index']})",
        flush=True,
    )
    print(f"[offline-stress] output={output_json}", flush=True)
    started_at = time.perf_counter()

    if stream_subprocess:
        process = subprocess.Popen(
            cmd,
            cwd=str(vla0_root),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        with open(log_path, "w", encoding="utf-8") as handle:
            for raw_line in process.stdout:
                print(raw_line.rstrip(), flush=True)
                handle.write(raw_line)
        process.stdout.close()
        returncode = process.wait()
    else:
        with open(log_path, "w", encoding="utf-8", buffering=1) as handle:
            process = subprocess.Popen(
                cmd,
                cwd=str(vla0_root),
                env=env,
                stdout=handle,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            last_heartbeat_at = -heartbeat_seconds
            while True:
                returncode = process.poll()
                now = time.perf_counter()
                if returncode is not None:
                    break
                if now - last_heartbeat_at >= heartbeat_seconds:
                    print(
                        f"[offline-stress] heartbeat {stratum['label']} | "
                        f"elapsed={format_duration(now - started_at)} | "
                        f"last='{last_nonempty_line(log_path)}'",
                        flush=True,
                    )
                    last_heartbeat_at = now
                time.sleep(1.0)

    elapsed_seconds = time.perf_counter() - started_at
    result = {
        "label": stratum["label"],
        "start_index": stratum["start_index"],
        "end_index": stratum["end_index"],
        "num_samples": stratum["num_samples"],
        "returncode": returncode,
        "status": "success" if returncode == 0 else "runtime_error",
        "elapsed_seconds": elapsed_seconds,
        "output_json": str(output_json),
        "log_path": str(log_path),
    }
    print(
        f"[offline-stress] finished {stratum['label']} | "
        f"status={result['status']} | elapsed={format_duration(elapsed_seconds)}",
        flush=True,
    )
    return result


def summarize_mode(mode_name: str, mode_results: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "num_samples": len(mode_results),
        "mean_load_seconds": statistics.mean(item["load_seconds"] for item in mode_results),
        "mean_generation_seconds": statistics.mean(item["generation_seconds"] for item in mode_results),
        "median_generation_seconds": statistics.median(item["generation_seconds"] for item in mode_results),
        "p95_generation_seconds": percentile(
            [item["generation_seconds"] for item in mode_results], 95.0
        ),
        "mean_cuda_memory_allocated_mb": statistics.mean(
            item["cuda_memory_allocated_mb"] for item in mode_results
        ),
        "mean_cuda_memory_reserved_mb": statistics.mean(
            item["cuda_memory_reserved_mb"] for item in mode_results
        ),
        "mean_cuda_max_memory_allocated_mb": statistics.mean(
            item["cuda_max_memory_allocated_mb"] for item in mode_results
        ),
        "peak_cuda_max_memory_allocated_mb": max(
            item["cuda_max_memory_allocated_mb"] for item in mode_results
        ),
        "mean_token_count": statistics.mean(item["pred_token_count"] for item in mode_results),
    }

    if mode_name == "bf16":
        return summary

    drift_items = [item["vs_bf16"] for item in mode_results if item.get("vs_bf16") is not None]
    if drift_items:
        maes = [item["mae"] for item in drift_items]
        mses = [item["mse"] for item in drift_items]
        max_abs_values = [item["max_abs"] for item in drift_items]
        exact_matches = sum(1 for item in mode_results if item.get("exact_text_match_bf16"))
        summary.update(
            {
                "mean_mae_vs_bf16": statistics.mean(maes),
                "median_mae_vs_bf16": statistics.median(maes),
                "p95_mae_vs_bf16": percentile(maes, 95.0),
                "mean_mse_vs_bf16": statistics.mean(mses),
                "max_abs_vs_bf16": max(max_abs_values),
                "exact_text_match_rate_vs_bf16": exact_matches / len(mode_results),
            }
        )
    return summary


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    rank = (len(ordered) - 1) * (pct / 100.0)
    low = math.floor(rank)
    high = math.ceil(rank)
    if low == high:
        return ordered[low]
    frac = rank - low
    return ordered[low] * (1.0 - frac) + ordered[high] * frac


def collect_worst_cases(
    mode_results: list[dict[str, Any]],
    *,
    worst_k: int,
) -> list[dict[str, Any]]:
    rows = []
    for item in mode_results:
        drift = item.get("vs_bf16")
        if not drift:
            continue
        rows.append(
            {
                "sample_index": item["sample_index"],
                "stratum": item.get("stratum"),
                "instruction": item["instruction"],
                "generation_seconds": item["generation_seconds"],
                "pred_action_txt": item["pred_action_txt"],
                "gt_action_text": item["gt_action_text"],
                "mae": drift["mae"],
                "mse": drift["mse"],
                "max_abs": drift["max_abs"],
                "exact_text_match_bf16": item.get("exact_text_match_bf16"),
            }
        )
    rows.sort(key=lambda row: (row["mae"], row["max_abs"]), reverse=True)
    return rows[:worst_k]


def main() -> None:
    args = parse_args()
    vla0_root = Path(args.vla0_root).expanduser().resolve()
    compare_batch_script = vla0_root / "scripts" / "compare_vla0_generation_batch.py"
    if not compare_batch_script.exists():
        raise FileNotFoundError(
            f"Missing compare_vla0_generation_batch.py at: {compare_batch_script}"
        )
    results_dir = Path(args.results_dir)
    raw_dir = results_dir / "raw"
    reports_dir = results_dir / "reports"
    raw_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    if args.device.startswith("cuda"):
        try:
            import torch  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "CUDA benchmark requested but torch is not importable. Run this in the qwen env."
            ) from exc
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA device requested, but torch.cuda.is_available() is False")

    dataset_len = get_dataset_length(vla0_root, args.checkpoint, args.split, args.lerobot_repo_id)
    strata = build_strata(
        dataset_len=dataset_len,
        num_strata=args.num_strata,
        samples_per_stratum=args.samples_per_stratum,
    )

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    modes_tag = "_".join(args.load_modes)
    run_id = f"offline_stress_{modes_tag}_{args.num_strata}x{args.samples_per_stratum}_{timestamp}"

    print(f"[offline-stress] dataset_len={dataset_len}", flush=True)
    print(f"[offline-stress] run_id={run_id}", flush=True)
    for stratum in strata:
        print(
            f"[offline-stress] stratum {stratum['label']}: "
            f"{stratum['start_index']}..{stratum['end_index']}",
            flush=True,
        )

    started_at = time.perf_counter()
    run_records = []
    payloads = []
    for stratum in strata:
        record = run_stratum(
            stratum=stratum,
            vla0_root=vla0_root,
            compare_batch_script=compare_batch_script,
            checkpoint=args.checkpoint,
            device=args.device,
            split=args.split,
            load_modes=args.load_modes,
            progress_every=args.progress_every,
            lerobot_repo_id=args.lerobot_repo_id,
            raw_dir=raw_dir,
            heartbeat_seconds=args.heartbeat_seconds,
            stream_subprocess=args.stream_subprocess,
        )
        run_records.append(record)
        if record["returncode"] != 0:
            break
        payloads.append(json.loads(Path(record["output_json"]).read_text()))

    elapsed_seconds = time.perf_counter() - started_at

    aggregate: dict[str, Any] = {
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "protocol": "vla0_offline_stress_benchmark_v1",
        "run_id": run_id,
        "checkpoint": args.checkpoint,
        "device": args.device,
        "split": args.split,
        "lerobot_repo_id": args.lerobot_repo_id,
        "load_modes": args.load_modes,
        "dataset_len": dataset_len,
        "num_strata": args.num_strata,
        "samples_per_stratum": args.samples_per_stratum,
        "total_target_samples": args.num_strata * args.samples_per_stratum,
        "elapsed_seconds": elapsed_seconds,
        "status": "success" if len(run_records) == len(strata) and all(r["returncode"] == 0 for r in run_records) else "runtime_error",
        "strata": strata,
        "runs": run_records,
        "modes": {},
    }

    if payloads and aggregate["status"] == "success":
        mode_samples: dict[str, list[dict[str, Any]]] = {mode: [] for mode in args.load_modes}
        per_stratum_summary: dict[str, dict[str, Any]] = {mode: {} for mode in args.load_modes}
        for record, payload in zip(run_records, payloads):
            label = record["label"]
            for mode in args.load_modes:
                block = payload["modes"][mode]
                for sample in block["samples"]:
                    sample["stratum"] = label
                mode_samples[mode].extend(block["samples"])
                per_stratum_summary[mode][label] = block["summary"]

        for mode in args.load_modes:
            aggregate["modes"][mode] = {
                "summary": summarize_mode(mode, mode_samples[mode]),
                "per_stratum": per_stratum_summary[mode],
                "worst_cases": collect_worst_cases(mode_samples[mode], worst_k=args.worst_k),
            }

    summary_path = reports_dir / f"{run_id}.json"
    summary_path.write_text(json.dumps(aggregate, indent=2))

    print()
    print(f"[offline-stress] completed in {format_duration(elapsed_seconds)}", flush=True)
    print(f"[offline-stress] summary={summary_path}", flush=True)
    print(json.dumps(aggregate, indent=2)[:20000], flush=True)


if __name__ == "__main__":
    main()
