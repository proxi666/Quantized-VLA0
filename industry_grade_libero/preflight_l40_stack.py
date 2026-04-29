#!/usr/bin/env python3
"""Preflight checks for a remote multi-GPU VLA-0 LIBERO machine."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vla0-root", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output-root", default="preflight_l40")
    parser.add_argument("--gpus", default="0,1,2,3")
    parser.add_argument("--skip-rollout", action="store_true")
    return parser.parse_args()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def run(cmd: list[str], env: dict[str, str] | None = None, cwd: str | None = None) -> dict[str, Any]:
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=900,
    )
    return {
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-8000:],
        "stderr": proc.stderr[-8000:],
    }


def gpu_env(gpu_id: str) -> dict[str, str]:
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = gpu_id
    env.setdefault("MUJOCO_GL", "egl")
    env.setdefault("PYOPENGL_PLATFORM", "egl")
    env.setdefault("MUJOCO_EGL_DEVICE_ID", "0")
    env.setdefault("TOKENIZERS_PARALLELISM", "false")
    return env


def main() -> int:
    args = parse_args()
    output_root = Path(args.output_root).expanduser().resolve()
    vla0_root = Path(args.vla0_root).expanduser().resolve()
    checkpoint = Path(args.checkpoint).expanduser().resolve()
    gpus = [item.strip() for item in args.gpus.split(",") if item.strip()]
    output_root.mkdir(parents=True, exist_ok=True)

    hardware = {
        "created_at": datetime.now().replace(microsecond=0).isoformat(),
        "python": sys.version,
        "vla0_root": str(vla0_root),
        "checkpoint": str(checkpoint),
        "gpus_requested": gpus,
        "disk_usage_output_root": shutil.disk_usage(output_root)._asdict(),
        "checkpoint_exists": checkpoint.exists(),
        "vla0_eval_exists": (vla0_root / "eval" / "eval_libero.py").exists(),
    }
    if shutil.which("nvidia-smi"):
        hardware["nvidia_smi"] = run(["nvidia-smi"])
        hardware["nvidia_smi_l"] = run(["nvidia-smi", "-L"])
    else:
        hardware["nvidia_smi"] = {"returncode": 127, "stderr": "nvidia-smi not found"}

    torch_probe = (
        "import torch, json\n"
        "print(json.dumps({'cuda': torch.cuda.is_available(), "
        "'count': torch.cuda.device_count(), "
        "'names': [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]}))\n"
    )
    hardware["torch"] = run([sys.executable, "-c", torch_probe])
    write_json(output_root / "hardware.json", hardware)

    report = {
        "created_at": datetime.now().replace(microsecond=0).isoformat(),
        "hardware_json": str(output_root / "hardware.json"),
        "checks": [],
    }
    report["checks"].append(
        {
            "name": "checkpoint_exists",
            "ok": checkpoint.exists(),
            "detail": str(checkpoint),
        }
    )
    report["checks"].append(
        {
            "name": "vla0_eval_exists",
            "ok": (vla0_root / "eval" / "eval_libero.py").exists(),
            "detail": str(vla0_root / "eval" / "eval_libero.py"),
        }
    )

    if not args.skip_rollout:
        smoke_root = output_root / "smoke_rollout"
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "run_multigpu_libero.py"),
            "--vla0-root",
            str(vla0_root),
            "--checkpoint",
            str(checkpoint),
            "--output-root",
            str(smoke_root),
            "--gpus",
            ",".join(gpus[:1]),
            "--modes",
            "bf16",
            "--suites",
            "libero_spatial",
            "--task-id-count",
            "50",
            "--smoke",
            "--resume",
        ]
        smoke = run(cmd, env=gpu_env(gpus[0]), cwd=str(vla0_root))
        report["smoke_rollout"] = smoke
        report["checks"].append(
            {
                "name": "one_episode_bf16_libero_smoke",
                "ok": smoke["returncode"] == 0,
                "detail": str(smoke_root),
            }
        )

    report["ok"] = all(item["ok"] for item in report["checks"])
    write_json(output_root / "preflight_report.json", report)
    print(json.dumps({"ok": report["ok"], "output_root": str(output_root)}, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

