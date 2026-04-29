#!/usr/bin/env python3
"""Merge multi-GPU VLA-0 LIBERO shard results into paper-ready summaries."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--expected-episodes-per-task", type=int, default=50)
    return parser.parse_args()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def status_for(job: dict[str, Any]) -> dict[str, Any]:
    status_path = Path(job["status_path"])
    if not status_path.exists():
        return {"status": "missing_status", "job_id": job["job_id"]}
    try:
        return read_json(status_path)
    except Exception as exc:
        return {"status": "bad_status", "job_id": job["job_id"], "error": str(exc)}


def result_counts(job: dict[str, Any]) -> tuple[int, int]:
    result_path = Path(job["results_json_path"])
    if not result_path.exists():
        return 0, 0
    data = read_json(result_path)
    return int(data.get("success", 0)), int(data.get("failure", 0))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    args = parse_args()
    output_root = Path(args.output_root).expanduser().resolve()
    manifest = read_json(output_root / "manifest.json")
    merged_root = output_root / "merged"
    failures = []
    shard_rows = []
    per_task = defaultdict(lambda: {"success": 0, "failure": 0, "shards": 0})

    for job in manifest["jobs"]:
        status = status_for(job)
        success, failure = result_counts(job)
        total = success + failure
        row = {
            "job_id": job["job_id"],
            "mode": job["mode"],
            "suite": job["suite"],
            "task_name": job["task_name"],
            "task_id_index": job["task_id_index"],
            "task_id_count": job["task_id_count"],
            "gpu_id": job["gpu_id"],
            "status": status.get("status"),
            "success": success,
            "failure": failure,
            "episodes": total,
            "elapsed_seconds": status.get("elapsed_seconds"),
            "results_json_path": job["results_json_path"],
            "status_path": job["status_path"],
        }
        shard_rows.append(row)
        if status.get("status") != "success" or total == 0:
            failures.append(row | {"error": status.get("error", "")})
            continue
        key = (job["mode"], job["suite"], job["task_name"])
        per_task[key]["success"] += success
        per_task[key]["failure"] += failure
        per_task[key]["shards"] += 1

    per_task_rows = []
    incomplete = []
    for (mode, suite, task_name), stats in sorted(per_task.items()):
        episodes = stats["success"] + stats["failure"]
        rate = stats["success"] / episodes if episodes else 0.0
        row = {
            "mode": mode,
            "suite": suite,
            "task_name": task_name,
            "success": stats["success"],
            "failure": stats["failure"],
            "episodes": episodes,
            "success_rate": rate,
            "shards": stats["shards"],
        }
        per_task_rows.append(row)
        if episodes != args.expected_episodes_per_task:
            incomplete.append(row)

    per_suite = defaultdict(lambda: {"success": 0, "failure": 0, "tasks": 0})
    for row in per_task_rows:
        key = (row["mode"], row["suite"])
        per_suite[key]["success"] += row["success"]
        per_suite[key]["failure"] += row["failure"]
        per_suite[key]["tasks"] += 1

    per_suite_rows = []
    for (mode, suite), stats in sorted(per_suite.items()):
        episodes = stats["success"] + stats["failure"]
        per_suite_rows.append(
            {
                "mode": mode,
                "suite": suite,
                "success": stats["success"],
                "failure": stats["failure"],
                "episodes": episodes,
                "success_rate": stats["success"] / episodes if episodes else 0.0,
                "tasks": stats["tasks"],
            }
        )

    total_success = sum(row["success"] for row in per_task_rows)
    total_failure = sum(row["failure"] for row in per_task_rows)
    summary = {
        "created_at": datetime.now().replace(microsecond=0).isoformat(),
        "output_root": str(output_root),
        "manifest_jobs": len(manifest["jobs"]),
        "total_success": total_success,
        "total_failure": total_failure,
        "total_episodes": total_success + total_failure,
        "failed_or_missing_shards": len(failures),
        "incomplete_tasks": len(incomplete),
        "complete": len(failures) == 0 and len(incomplete) == 0,
        "per_task": per_task_rows,
        "per_suite": per_suite_rows,
    }

    write_json(merged_root / "online_results_full.json", summary)
    write_json(merged_root / "failures.json", {"failures": failures, "incomplete": incomplete})
    write_csv(
        merged_root / "per_task_results.csv",
        per_task_rows,
        ["mode", "suite", "task_name", "success", "failure", "episodes", "success_rate", "shards"],
    )
    write_csv(
        merged_root / "per_suite_results.csv",
        per_suite_rows,
        ["mode", "suite", "success", "failure", "episodes", "success_rate", "tasks"],
    )
    write_csv(
        merged_root / "shard_results.csv",
        shard_rows,
        [
            "job_id",
            "mode",
            "suite",
            "task_name",
            "task_id_index",
            "task_id_count",
            "gpu_id",
            "status",
            "success",
            "failure",
            "episodes",
            "elapsed_seconds",
            "results_json_path",
            "status_path",
        ],
    )

    lines = [
        "# Multi-GPU LIBERO Summary",
        "",
        f"- Complete: `{summary['complete']}`",
        f"- Total episodes: `{summary['total_episodes']}`",
        f"- Failed/missing shards: `{summary['failed_or_missing_shards']}`",
        f"- Incomplete tasks: `{summary['incomplete_tasks']}`",
        "",
        "## Suite Results",
        "",
        "| Mode | Suite | Success | Failure | Episodes | Success Rate |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in per_suite_rows:
        lines.append(
            f"| {row['mode']} | {row['suite']} | {row['success']} | {row['failure']} | "
            f"{row['episodes']} | {100 * row['success_rate']:.1f}% |"
        )
    lines.append("")
    lines.append("## Completeness")
    lines.append("")
    if failures or incomplete:
        lines.append("Some shards or tasks are incomplete. See `failures.json`.")
    else:
        lines.append("All expected shards and task totals are complete.")
    (merged_root / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({k: summary[k] for k in ["complete", "total_episodes", "failed_or_missing_shards", "incomplete_tasks"]}, indent=2))
    return 0 if summary["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

