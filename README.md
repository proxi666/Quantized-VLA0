# Quantized-VLA0

Artifact repository for the ICRA 2026 workshop extended abstract:

**Quantization as an Inference-Stage Decision in the VLA Pipeline: A Workshop Extended Abstract on VLA-0 Reliability and Runtime**

This repo packages the final paper, figures, benchmark configuration, cleaned result summaries, and lightweight Python utilities used to organize and report the study.

## What This Repository Contains

- the workshop paper PDF
- the per-task online result JSONs for `BF16`, `INT8`, and `NF4`
- the final offline stress-benchmark report on an RTX 3070 8 GB GPU
- clean summary JSONs for quick downstream parsing
- a six-task benchmark config
- small Python scripts to:
  - regenerate the reported summary tables from the released JSONs
  - print the online evaluation commands used in the study
  - rerun the stratified offline stress benchmark against an external VLA-0 checkout

This repository is intentionally curated. It does **not** include:

- model weights
- dataset caches
- the full notebook history
- every intermediate log generated during experimentation

## Main Findings

### Online LIBERO benchmark

Matched setup:

- 6 tasks total
- 2 goal, 2 object, 2 spatial
- 10 episodes per task
- `action_horizon = 1`
- `ensemble_prediction = 8`

| Mode | Success | Failure | Success rate |
|---|---:|---:|---:|
| BF16 | 58 | 2 | 96.7% |
| INT8 | 58 | 2 | 96.7% |
| NF4 | 49 | 11 | 81.7% |

The largest task-level degradation is:

- `pick_up_the_cream_cheese_and_place_it_in_the_basket`
  - BF16: `10/10`
  - INT8: `9/10`
  - NF4: `3/10`

### Offline stress benchmark

Matched setup:

- 180 samples
- 6 strata × 30 samples
- local RTX 3070 8 GB

| Mode | Peak VRAM (MB) | Mean generation time (s) | Drift signal vs BF16 | Max deviation |
|---|---:|---:|---|---:|
| BF16 | 7,233 | 6.86 | baseline | - |
| INT8 | 6,608 | 28.96 | mean MAE `0.0169` | `2.0` |
| NF4 | 6,565 | 10.04 | mean MAE `0.9636`* | `9,374.95` |

\* NF4 mean MAE is dominated by a rare catastrophic outlier. Median MAE is `0.0298`.

## Repository Layout

```text
Quantized-VLA0/
├── paper/
│   └── icra2026_vla_pipeline.pdf
├── figures/
│   ├── generate_pertask_figure.py
│   ├── vla0_pertask_results.pdf
│   └── vla0_pertask_results.png
├── configs/
│   └── libero_six_task_benchmark.json
├── results/
│   ├── online/
│   │   ├── bf16/
│   │   ├── int8/
│   │   ├── nf4/
│   │   └── online_results_clean.json
│   ├── offline/
│   │   ├── offline_stress_bf16_int8_nf4_6x30.json
│   │   └── offline_stress_summary_clean.json
│   └── reports/
│       ├── ACTIVE_RESULTS_SYNTHESIS_DETAILED.md
│       ├── RESULT_REPORT_SUMMARY.md
│       └── offline_stress_benchmark_brief_20260323.md
└── scripts/
    ├── generate_eval_commands.py
    ├── run_offline_stress_benchmark.py
    └── summarize_release_results.py
```

## Quick Start

### 1. Read the paper

- [`paper/icra2026_vla_pipeline.pdf`](paper/icra2026_vla_pipeline.pdf)

### 2. Regenerate the summary tables from the released JSONs

```bash
python scripts/summarize_release_results.py
```

### 3. Print the online evaluation commands used in the study

This expects a separate local checkout of the VLA-0 codebase.

```bash
python scripts/generate_eval_commands.py \
  --vla0-root /path/to/vla0 \
  --mode bf16
```

For INT8, the script prints the split `5 + 5` commands used to reconstruct each 10-episode result.

### 4. Rerun the offline stress benchmark

This also expects a separate local VLA-0 checkout with the original evaluation code available.

```bash
python scripts/run_offline_stress_benchmark.py \
  --vla0-root /path/to/vla0 \
  --checkpoint /path/to/vla0/checkpoints/vla0-libero/model_last \
  --device cuda:0 \
  --samples-per-stratum 30
```

## Notes On Reproducibility

- The released online JSONs are the final per-task summaries used in the paper.
- `results/online/online_results_clean.json` and `results/offline/offline_stress_summary_clean.json` provide machine-friendly summaries without machine-local path clutter.
- Three NF4 tasks were reconstructed from preserved local result files, so their success/failure counts are complete but their full online runtime traces are not.
- The offline stress benchmark is the cleanest place to reproduce the latency, VRAM, and outlier analysis from the paper.
- This repository reports the study exactly as run; it is not an upstream VLA-0 fork.

## Citation

If this repository is useful, please cite the workshop abstract and link to this artifact repo.

See [`CITATION.cff`](CITATION.cff).
