#!/usr/bin/env python3
"""Summarize the released Quantized-VLA0 result JSONs."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ONLINE_ROOT = REPO_ROOT / "results" / "online"
OFFLINE_REPORT = REPO_ROOT / "results" / "offline" / "offline_stress_bf16_int8_nf4_6x30.json"


def load_online_rows() -> list[dict]:
    rows = []
    for path in sorted(ONLINE_ROOT.rglob("*.json")):
        data = json.loads(path.read_text())
        task = data["task_specs"][0]
        rollout = data["rollouts"][0]
        rows.append(
            {
                "mode": path.parent.name,
                "suite": task["task_suite_name"],
                "task_name": task["task_name"],
                "success": rollout["success"],
                "failure": rollout["failure"],
                "elapsed_seconds": rollout.get("elapsed_seconds"),
                "path": path.relative_to(REPO_ROOT).as_posix(),
            }
        )
    return rows


def print_online_summary(rows: list[dict]) -> None:
    by_mode = defaultdict(lambda: {"success": 0, "failure": 0})
    for row in rows:
        by_mode[row["mode"]]["success"] += row["success"]
        by_mode[row["mode"]]["failure"] += row["failure"]

    print("## Online aggregate")
    print("| Mode | Success | Failure | Success rate |")
    print("|---|---:|---:|---:|")
    for mode in ["bf16", "int8", "nf4"]:
        stats = by_mode[mode]
        total = stats["success"] + stats["failure"]
        rate = 100.0 * stats["success"] / total
        print(f"| {mode.upper()} | {stats['success']} | {stats['failure']} | {rate:.1f}% |")
    print()

    print("## Per-task online results")
    print("| Suite | Task | BF16 | INT8 | NF4 |")
    print("|---|---|---:|---:|---:|")
    grouped = defaultdict(dict)
    for row in rows:
        grouped[(row["suite"], row["task_name"])][row["mode"]] = row
    for suite, task_name in sorted(grouped):
        modes = grouped[(suite, task_name)]

        def fmt(mode: str) -> str:
            row = modes[mode]
            return f"{row['success']}/{row['failure'] + row['success']}"

        print(f"| `{suite}` | `{task_name}` | {fmt('bf16')} | {fmt('int8')} | {fmt('nf4')} |")
    print()


def print_offline_summary() -> None:
    data = json.loads(OFFLINE_REPORT.read_text())
    print("## Offline stress benchmark")
    print("| Mode | Samples | Peak VRAM (MB) | Mean generation time (s) | Mean MAE vs BF16 | p95 MAE vs BF16 | Max deviation |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for mode in ["bf16", "int8", "nf4"]:
        summary = data["modes"][mode]["summary"]
        mean_mae = summary.get("mean_mae_vs_bf16")
        p95_mae = summary.get("p95_mae_vs_bf16")
        max_dev = summary.get("max_abs_vs_bf16")
        def fmt(value):
            return "-" if value is None else f"{value:.4f}" if isinstance(value, float) else str(value)
        print(
            f"| {mode.upper()} | {summary['num_samples']} | "
            f"{summary['peak_cuda_max_memory_allocated_mb']:.0f} | "
            f"{summary['mean_generation_seconds']:.2f} | "
            f"{fmt(mean_mae)} | {fmt(p95_mae)} | {fmt(max_dev)} |"
        )
    print()


def main() -> None:
    rows = load_online_rows()
    print_online_summary(rows)
    print_offline_summary()


if __name__ == "__main__":
    main()
