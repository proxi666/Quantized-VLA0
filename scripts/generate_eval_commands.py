#!/usr/bin/env python3
"""Print the online evaluation commands used in the Quantized-VLA0 study.

This script does not run evaluation by itself. It prints the exact command
templates for a separate VLA-0 checkout.
"""

from __future__ import annotations

import argparse
import json
import shlex
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "configs" / "libero_six_task_benchmark.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vla0-root", required=True, help="Path to the external VLA-0 checkout.")
    parser.add_argument(
        "--checkpoint",
        help="Optional explicit checkpoint path. Defaults to <vla0-root>/checkpoints/vla0-libero/model_last.",
    )
    parser.add_argument(
        "--mode",
        default="all",
        choices=["all", "bf16", "nf4", "int8"],
        help="Which mode commands to print.",
    )
    parser.add_argument(
        "--suite",
        choices=["libero_goal", "libero_object", "libero_spatial"],
        help="Optional suite filter.",
    )
    parser.add_argument("--device", default="cuda:0")
    return parser.parse_args()


def quote(parts: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in parts)


def build_base_command(
    *,
    vla0_root: Path,
    checkpoint: Path,
    device: str,
    mode: str,
    suite: str,
    task_name: str,
    action_horizon: int,
    ensemble_prediction: int,
    seed: int,
    task_id_index: int,
    task_id_count: int,
) -> list[str]:
    return [
        "python",
        "-u",
        str(vla0_root / "eval" / "eval_libero.py"),
        "--model_path",
        str(checkpoint),
        "--device",
        device,
        "--load-mode",
        mode,
        "--task_suite_name",
        suite,
        "--task_name",
        task_name,
        "--action_horizon",
        str(action_horizon),
        "--ensemble_prediction",
        str(ensemble_prediction),
        "--num_steps",
        "0",
        "--start_seed",
        str(seed),
        "--task_id_index",
        str(task_id_index),
        "--task_id_count",
        str(task_id_count),
        "--no-torch-compile",
    ]


def main() -> None:
    args = parse_args()
    cfg = json.loads(CONFIG_PATH.read_text())
    vla0_root = Path(args.vla0_root).expanduser().resolve()
    checkpoint = (
        Path(args.checkpoint).expanduser().resolve()
        if args.checkpoint
        else vla0_root / "checkpoints" / "vla0-libero" / "model_last"
    )

    modes = ["bf16", "nf4", "int8"] if args.mode == "all" else [args.mode]
    tasks = cfg["tasks"]
    if args.suite:
        tasks = [task for task in tasks if task["suite"] == args.suite]

    print("# Quantized-VLA0 evaluation commands")
    print(f"# vla0-root: {vla0_root}")
    print(f"# checkpoint: {checkpoint}")
    print()

    for mode in modes:
        print(f"## {mode}")
        for task in tasks:
            suite = task["suite"]
            task_name = task["task_name"]
            print(f"# {suite} :: {task_name}")
            if mode == "int8":
                for part_idx, task_id_index in enumerate([0, 1], start=1):
                    cmd = build_base_command(
                        vla0_root=vla0_root,
                        checkpoint=checkpoint,
                        device=args.device,
                        mode=mode,
                        suite=suite,
                        task_name=task_name,
                        action_horizon=cfg["action_horizon"],
                        ensemble_prediction=cfg["ensemble_prediction"],
                        seed=cfg["seed"],
                        task_id_index=task_id_index,
                        task_id_count=10,
                    )
                    print(f"# part {part_idx} / 2")
                    print(quote(cmd))
            else:
                cmd = build_base_command(
                    vla0_root=vla0_root,
                    checkpoint=checkpoint,
                    device=args.device,
                    mode=mode,
                    suite=suite,
                    task_name=task_name,
                    action_horizon=cfg["action_horizon"],
                    ensemble_prediction=cfg["ensemble_prediction"],
                    seed=cfg["seed"],
                    task_id_index=0,
                    task_id_count=5,
                )
                print(quote(cmd))
            print()


if __name__ == "__main__":
    main()
