# Industry-Grade Multi-GPU LIBERO Evaluation

This folder contains a notebook-free runner for scaling the Quantized-VLA0 online LIBERO benchmark on a remote multi-GPU machine.

The intended machine is a datacenter GPU stack such as 4x L40/L40S/A100-class GPUs. The runner treats each GPU as an independent rollout worker. It does not use tensor parallelism because VLA-0 fits on one 40-48 GB GPU and LIBERO online rollouts are closed-loop simulator sequences.

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

## Remote Setup Assumption

The remote machine should already have:

- a VLA-0 checkout
- the VLA-0 LIBERO checkpoint
- a working Python environment for VLA-0
- MuJoCo/robosuite/LIBERO installed
- working headless EGL rendering

Recommended environment variables:

```bash
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export TOKENIZERS_PARALLELISM=false
```

The worker sets `CUDA_VISIBLE_DEVICES=<physical_gpu_id>` and `MUJOCO_EGL_DEVICE_ID=0` per process.

## 1. Preflight

Run this before starting the full benchmark:

```bash
python industry_grade_libero/preflight_l40_stack.py \
  --vla0-root /path/to/vla0 \
  --checkpoint /path/to/vla0/checkpoints/vla0-libero/model_last \
  --output-root /path/to/preflight_l40 \
  --gpus 0,1,2,3
```

This writes:

```text
hardware.json
preflight_report.json
```

It also runs a one-episode BF16 LIBERO smoke test unless `--skip-rollout` is used.

## 2. Dry Run

Generate the full manifest without launching workers:

```bash
python industry_grade_libero/run_multigpu_libero.py \
  --vla0-root /path/to/vla0 \
  --checkpoint /path/to/vla0/checkpoints/vla0-libero/model_last \
  --output-root /path/to/vla0_quant_full_runs \
  --gpus 0,1,2,3 \
  --dry-run
```

Expected default manifest:

```text
1200 shard jobs
6000 total rollouts
```

## 3. Full Run

```bash
python industry_grade_libero/run_multigpu_libero.py \
  --vla0-root /path/to/vla0 \
  --checkpoint /path/to/vla0/checkpoints/vla0-libero/model_last \
  --output-root /path/to/vla0_quant_full_runs \
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

## 4. Merge Results

```bash
python industry_grade_libero/merge_results.py \
  --output-root /path/to/vla0_quant_full_runs
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

## Practical Notes

- Use one worker per GPU first. Do not start with multiple LIBERO renderers per GPU.
- Keep videos for the first full run. They are useful for audit and debugging.
- If disk becomes an issue, merge first, then prune videos manually after preserving `results.json`, `status.json`, and `summary.md`.
- If a worker fails, fix the environment or failing task and rerun the same command with `--resume`.

