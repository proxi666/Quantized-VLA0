# Industry-Grade Multi-GPU LIBERO Evaluation

This folder contains a notebook-free runner for scaling the Quantized-VLA0 online LIBERO benchmark on a remote multi-GPU machine.

The intended machine is a datacenter GPU stack such as 4x L40/L40S/A100-class GPUs. The runner treats each GPU as an independent rollout worker. It does not use tensor parallelism because VLA-0 fits on one 40-48 GB GPU and LIBERO online rollouts are closed-loop simulator sequences.

Use this README as the remote runbook. The commands assume the remote machine has two repos:

```text
/workspace/vla0              # external VLA-0 checkout with checkpoint and dependencies
/workspace/Quantized-VLA0    # this artifact repo
```

If your paths differ, replace `/workspace/...` in the commands.

## Default Benchmark

The default full benchmark is:

```text
3 modes x 4 suites x 10 tasks x 50 episodes
= 6000 online rollouts
```

Modes:

```text
bf16, int8, nf4
```

Suites:

```text
libero_spatial, libero_object, libero_goal, libero_10
```

Evaluation settings:

```text
seed = 7
action_horizon = 1
ensemble_prediction = 8
task_id_count = 10
```

`task_id_count=10` splits each 50-episode LIBERO task into 10 shards of 5 episodes each.

## Required Remote Setup

The remote machine should already have:

- a VLA-0 checkout
- the VLA-0 LIBERO checkpoint
- a working Python environment for VLA-0
- MuJoCo/robosuite/LIBERO installed
- working headless EGL rendering

Minimal expected layout:

```text
/workspace/vla0/
  eval/eval_libero.py
  rv_train/
  libs/RoboVerse/
  checkpoints/vla0-libero/model_last/

/workspace/Quantized-VLA0/
  industry_grade_libero/
```

Before running, activate the same Python environment that can run VLA-0:

```bash
cd /workspace/Quantized-VLA0
source /path/to/your/env/bin/activate
```

For conda, use:

```bash
conda activate qwen
```

Recommended environment variables for the shell:

```bash
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export TOKENIZERS_PARALLELISM=false
```

The worker sets `CUDA_VISIBLE_DEVICES=<physical_gpu_id>` and `MUJOCO_EGL_DEVICE_ID=0` per process.

## 0. Quick Hardware Check

Run:

```bash
nvidia-smi -L
nvidia-smi
python - <<'PY'
import torch
print("cuda:", torch.cuda.is_available())
print("gpu_count:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    print(i, torch.cuda.get_device_name(i), round(p.total_memory / 1024**3, 1), "GB")
PY
```

Expected:

```text
4 visible GPUs
each GPU roughly 40-48 GB
torch.cuda.is_available() == True
```

If this fails, fix CUDA/PyTorch before running LIBERO.

## 1. Preflight

Run this before starting the full benchmark:

```bash
python industry_grade_libero/preflight_l40_stack.py \
  --vla0-root /workspace/vla0 \
  --checkpoint /workspace/vla0/checkpoints/vla0-libero/model_last \
  --output-root /workspace/vla0_quant_preflight \
  --gpus 0,1,2,3
```

This writes:

```text
/workspace/vla0_quant_preflight/hardware.json
/workspace/vla0_quant_preflight/preflight_report.json
```

It also runs a one-episode BF16 LIBERO smoke test unless `--skip-rollout` is used.

Read the result:

```bash
cat /workspace/vla0_quant_preflight/preflight_report.json
```

Proceed only if `"ok": true`.

## 2. Dry Run

Generate the full manifest without launching workers:

```bash
python industry_grade_libero/run_multigpu_libero.py \
  --vla0-root /workspace/vla0 \
  --checkpoint /workspace/vla0/checkpoints/vla0-libero/model_last \
  --output-root /workspace/vla0_quant_full_runs \
  --gpus 0,1,2,3 \
  --dry-run
```

Expected default manifest:

```text
1200 shard jobs
6000 total rollouts
```

Check the manifest:

```bash
python - <<'PY'
import json
from pathlib import Path
m = json.loads(Path("/workspace/vla0_quant_full_runs/manifest.json").read_text())
print("jobs:", len(m["jobs"]))
print("expected_rollouts:", m["expected_rollouts"])
print("first_job:", m["jobs"][0])
PY
```

Expected:

```text
jobs: 1200
expected_rollouts: 6000
```

## 3. Four-GPU Smoke Run

Before launching all 1200 shards, run one shard per GPU:

```bash
python industry_grade_libero/run_multigpu_libero.py \
  --vla0-root /workspace/vla0 \
  --checkpoint /workspace/vla0/checkpoints/vla0-libero/model_last \
  --output-root /workspace/vla0_quant_smoke \
  --gpus 0,1,2,3 \
  --modes bf16 \
  --suites libero_spatial \
  --task-id-count 50 \
  --smoke \
  --resume
```

Then merge the smoke result:

```bash
python industry_grade_libero/merge_results.py \
  --output-root /workspace/vla0_quant_smoke \
  --expected-episodes-per-task 1
```

The smoke merge should report `complete: true`. If it fails, inspect:

```bash
ls -lh /workspace/vla0_quant_smoke/logs/
cat /workspace/vla0_quant_smoke/merged/failures.json
```

## 4. Full Run

```bash
python industry_grade_libero/run_multigpu_libero.py \
  --vla0-root /workspace/vla0 \
  --checkpoint /workspace/vla0/checkpoints/vla0-libero/model_last \
  --output-root /workspace/vla0_quant_full_runs \
  --gpus 0,1,2,3 \
  --modes bf16 int8 nf4 \
  --suites libero_spatial libero_object libero_goal libero_10 \
  --task-id-count 10 \
  --resume
```

Worker logs are written to:

```text
<output-root>/logs/worker_gpu_<id>.log
```

Each shard writes:

```text
<output-root>/runs/<mode>/<suite>/<task>/shard_<i>_of_<n>/results.json
<output-root>/runs/<mode>/<suite>/<task>/shard_<i>_of_<n>/status.json
```

Watch progress:

```bash
tail -f /workspace/vla0_quant_full_runs/logs/worker_gpu_0.log
```

Check all workers:

```bash
tail -n 40 /workspace/vla0_quant_full_runs/logs/worker_gpu_*.log
```

If the run is interrupted, rerun the exact same full command with `--resume`. Completed shards are skipped.

## 5. Merge Results

```bash
python industry_grade_libero/merge_results.py \
  --output-root /workspace/vla0_quant_full_runs
```

Merged outputs:

```text
merged/online_results_full.json
merged/per_task_results.csv
merged/per_suite_results.csv
merged/shard_results.csv
merged/summary.md
merged/failures.json
```

The merge step marks the benchmark incomplete unless every `(mode, suite, task)` has exactly 50 episodes.

Check the final summary:

```bash
cat /workspace/vla0_quant_full_runs/merged/summary.md
```

Expected full-run completion:

```text
Total episodes: 6000
Failed/missing shards: 0
Incomplete tasks: 0
```

## What To Send Back

After the run, send back these files first:

```text
/workspace/vla0_quant_preflight/hardware.json
/workspace/vla0_quant_preflight/preflight_report.json
/workspace/vla0_quant_full_runs/manifest.json
/workspace/vla0_quant_full_runs/merged/online_results_full.json
/workspace/vla0_quant_full_runs/merged/per_task_results.csv
/workspace/vla0_quant_full_runs/merged/per_suite_results.csv
/workspace/vla0_quant_full_runs/merged/shard_results.csv
/workspace/vla0_quant_full_runs/merged/summary.md
/workspace/vla0_quant_full_runs/merged/failures.json
```

If something fails, also send:

```text
/workspace/vla0_quant_full_runs/logs/
```

Do not send all videos unless needed. The videos can be very large.

## Common Failure Checks

If CUDA works but LIBERO fails at rendering, check EGL:

```bash
echo $MUJOCO_GL
echo $PYOPENGL_PLATFORM
echo $CUDA_VISIBLE_DEVICES
```

For this runner, worker processes should use:

```text
MUJOCO_GL=egl
PYOPENGL_PLATFORM=egl
MUJOCO_EGL_DEVICE_ID=0
```

If disk fills up:

1. Stop the run.
2. Run `merge_results.py`.
3. Preserve all `results.json`, `status.json`, `manifest.json`, and `merged/`.
4. Prune videos only after merged results are saved.

If one shard fails:

```bash
cat /workspace/vla0_quant_full_runs/merged/failures.json
```

Then rerun the full command with:

```bash
--resume
```

## Practical Notes

- Use one worker per GPU first. Do not start with multiple LIBERO renderers per GPU.
- Keep videos for the first full run. They are useful for audit and debugging.
- If disk becomes an issue, merge first, then prune videos manually after preserving `results.json`, `status.json`, and `summary.md`.
- If a worker fails, fix the environment or failing task and rerun the same command with `--resume`.
