# Active Results Synthesis

Date: 2026-03-29

## Scope

This document synthesizes the entire contents of `vla0/research/results/active/` as it exists now.

I read and combined all active artifacts:

- `87` files total
- `41` notebooks
- `28` JSON files
- `14` logs
- `2` markdown files
- `1` Python source file
- `1` Python bytecode file

The tree currently contains four main result groups:

- `kaggle_bf16`
- `kaggle_nf4`
- `kaggle_int8`
- `offline_test`

## Executive Summary

The important conclusions are:

1. `BF16` and `INT8` achieved the same final online success rate on the matched 6-task benchmark: `58/60 = 96.7%`.
2. `NF4` was clearly weaker online: `49/60 = 81.7%`.
3. The main NF4 failure is concentrated in the `libero_object` suite, especially `pick_up_the_cream_cheese_and_place_it_in_the_basket` with only `3/10`.
4. `INT8` is not a practical speed optimization in this stack. It preserved online success, but required far more runtime than BF16.
5. The offline stress benchmark explains why NF4 is dangerous: it is usually close to BF16, but it has a rare catastrophic outlier tail.
6. The offline benchmark also shows that INT8 is numerically stable relative to BF16, but it is much slower than both BF16 and NF4.
7. The goal suite is the most stable across all modes. The object suite is the most discriminative.

The strongest paper-level story from the active results is:

- `BF16` is the strongest practical baseline.
- `INT8` is accurate enough online and offline, but operationally too slow to be an attractive deployment choice under the current software stack.
- `NF4` is often close to BF16, but its rare large failures are strong enough to break object manipulation reliability.

## Inventory Summary

### File Counts By Top-Level Folder

| Folder | File count | What it contains |
|---|---:|---|
| `kaggle_bf16` | 17 | BF16 notebooks, logs, and final JSONs |
| `kaggle_nf4` | 15 | NF4 notebooks, recovered JSONs, and local probe artifacts |
| `kaggle_int8` | 38 | INT8 notebooks, split runs, final merged JSONs, and one partial local full-run log |
| `offline_test` | 17 | Offline stress benchmark code, logs, per-stratum JSONs, and final report |

### File Counts By Extension

| Extension | Count |
|---|---:|
| `.ipynb` | 41 |
| `.json` | 28 |
| `.log` | 14 |
| `.md` | 2 |
| `.py` | 1 |
| `.pyc` | 1 |

## Common Online Protocol Recovered From Notebooks

Across the BF16 and NF4 online notebooks, the matched benchmark protocol is consistent:

- `ACTION_HORIZON = 1`
- `ENSEMBLE_PREDICTION = 8`
- `TOTAL_LIBERO_INIT_STATES = 50`
- `ROLLOUT_EPISODES_PER_TASK = 10`
- one task per notebook
- one suite-task pair per final JSON

Across the INT8 split notebooks, the protocol was adapted to fit runtime constraints:

- same task definitions
- same `ACTION_HORIZON = 1`
- same `ENSEMBLE_PREDICTION = 8`
- `5 + 5` split execution
- `TASK_ID_INDEX = 0` or `1`
- each split covers `5` episodes
- merged JSONs reconstruct the full `10`-episode result

This split design is important operationally: it is the only reason the full 6-task INT8 online benchmark was completed in the active tree.

## Online Benchmark Results

### Per-Task Results

| Suite | Task | BF16 | NF4 | INT8 |
|---|---|---:|---:|---:|
| `libero_goal` | `open_the_middle_drawer_of_the_cabinet` | `10/10` | `9/10` | `10/10` |
| `libero_goal` | `put_the_bowl_on_the_stove` | `10/10` | `10/10` | `10/10` |
| `libero_object` | `pick_up_the_alphabet_soup_and_place_it_in_the_basket` | `9/10` | `8/10` | `10/10` |
| `libero_object` | `pick_up_the_cream_cheese_and_place_it_in_the_basket` | `10/10` | `3/10` | `9/10` |
| `libero_spatial` | `pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate` | `9/10` | `9/10` | `9/10` |
| `libero_spatial` | `pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate` | `10/10` | `10/10` | `10/10` |

### Aggregate Online Success

| Mode | Success | Failure | Success rate |
|---|---:|---:|---:|
| `BF16` | `58` | `2` | `96.7%` |
| `NF4` | `49` | `11` | `81.7%` |
| `INT8` | `58` | `2` | `96.7%` |

### Suite-Level Online Success

| Mode | Goal | Object | Spatial |
|---|---:|---:|---:|
| `BF16` | `20/20 = 100%` | `19/20 = 95%` | `19/20 = 95%` |
| `NF4` | `19/20 = 95%` | `11/20 = 55%` | `19/20 = 95%` |
| `INT8` | `20/20 = 100%` | `19/20 = 95%` | `19/20 = 95%` |

### Most Important Online Observation

NF4 is not uniformly bad.

It is:

- almost identical to BF16 on the goal suite
- almost identical to BF16 on the spatial suite
- substantially worse on the object suite

The entire NF4 aggregate drop is driven by the object tasks, and especially one task:

- `pick_up_the_cream_cheese_and_place_it_in_the_basket`
- `BF16: 10/10`
- `NF4: 3/10`
- `INT8: 9/10`

This is the cleanest online evidence that the quantization effect is real rather than random.

## Online Runtime Findings

### BF16 Known Total Runtime

All 6 BF16 final JSONs contain elapsed time.

- total known BF16 online runtime: `26.16 GPU-hours`

Suite breakdown:

- goal: `7.67 GPU-hours`
- object: `11.08 GPU-hours`
- spatial: `7.41 GPU-hours`

### NF4 Known Runtime

Only 3 of the 6 NF4 final task summaries retain elapsed time in their recovered JSONs.

- known NF4 runtime from recorded tasks: `25.03 GPU-hours`
- known elapsed tasks:
  - goal drawer
  - goal stove
  - object alphabet soup

For the three tasks recovered from local `results.json`, success/failure is preserved but elapsed time is not.

Even on the three tasks with elapsed data, NF4 is slower than BF16:

- goal drawer: `8.72h` vs `4.55h`
- goal stove: `5.01h` vs `3.12h`
- object alphabet soup: `11.31h` vs `6.48h`

So the active results do not support any claim that NF4 made the online benchmark faster in this software stack.

### INT8 Runtime

All 6 merged INT8 task JSONs contain elapsed time.

- total known INT8 online runtime: `96.50 GPU-hours`

Suite breakdown:

- goal: `29.16 GPU-hours`
- object: `38.85 GPU-hours`
- spatial: `28.49 GPU-hours`

INT8 therefore matched BF16 online success, but at roughly:

- `96.50 / 26.16 = 3.69x`

the measured BF16 total online runtime.

That is the single most important operational result for INT8.

## Operational Findings From Logs And Notebook Outputs

### 1. INT8 Split Execution Was Necessary

The INT8 notebook outputs show successful `5/5` and `4/5 + 5/5` half-runs:

- goal 1:
  - `g1p1 = 5/5`
  - `g1p2 = 5/5`
- goal 2:
  - `g2p1 = 5/5`
  - `g2p2 = 5/5`
- object 1:
  - `o1p1 = 5/5`
  - `o1p2 = 5/5`
- object 2:
  - `o2p1 = 4/5`
  - `o2p2 = 5/5`
- spatial 1:
  - `s1p1 = 5/5`
  - `s1p2 = 5/5`
- spatial 2:
  - `s2p1 = 4/5`
  - `s2p2 = 5/5`

These notebook-level split results are internally consistent with the merged final INT8 JSONs.

### 2. Full Local INT8 Online Runs Were Operationally Impractical

The partial local log:

- `kaggle_int8/object/local_runs/int8_object2_full_20260323_231046.log`

shows the unsplit full INT8 object run progressing only to around:

- `97/290`

before termination.

The tail contains:

- `Terminated`

This matches the broader runtime evidence:

- full unsplit INT8 online evaluation is too expensive to be the practical path
- split execution was the workable path

### 3. Dual-GPU Experiment Notebooks Exist, But No Successful Result Payload Is Present In `active/`

Two dual-GPU experiment notebooks are present:

- `kaggle_bf16/spatial/spartial1_dual_gpu_experiment.ipynb`
- `kaggle_int8/spatial/spartial1_dual_gpu_experiment.ipynb`

Their saved notebook JSONs contain configuration code but no successful result payload in the `active` tree. Based on the artifact set alone, they should be treated as experimental setup artifacts, not completed benchmark evidence.

### 4. NF4 Recovered Local Results Are Real, But Partly Missing Timing Metadata

The NF4 object cream-cheese and both NF4 spatial task summaries were reconstructed from local `results.json` outputs and saved as `*_localcopy.json`.

These recovered JSONs preserve:

- mode
- suite
- task
- success/failure

They do not preserve:

- elapsed runtime
- raw log path

This matters because the NF4 online accuracy numbers are complete, but the runtime accounting is only partial.

## Offline Stress Benchmark

### Protocol

The offline benchmark in `offline_test` is a stronger complementary evaluation axis than the online success table alone.

Recovered protocol:

- device: RTX 3070 8GB local machine
- modes: `bf16`, `int8`, `nf4`
- one mode loaded at a time
- `6` strata
- `30` samples per stratum
- `180` total samples
- same fixed sample set across all three modes
- outputs include:
  - load time
  - generation time
  - VRAM
  - MAE vs BF16
  - MSE vs BF16
  - p95 statistics
  - worst-case examples

The final offline report is:

- `offline_test/reports/offline_stress_bf16_int8_nf4_6x30_20260323_112236.json`

Total runtime:

- `9.15 hours`

### Aggregate Offline Results

| Mode | Samples | Mean generation | Peak VRAM | Mean MAE vs BF16 | Median MAE vs BF16 | p95 MAE vs BF16 | Max abs vs BF16 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `BF16` | `180` | `6.86s` | `7232.87 MB` | `-` | `-` | `-` | `-` |
| `INT8` | `180` | `28.96s` | `6607.99 MB` | `0.01693` | `0.01434` | `0.04109` | `2.0` |
| `NF4` | `180` | `10.04s` | `6564.76 MB` | `0.96360` | `0.02982` | `0.06818` | `9374.95` |

### Important Offline Interpretation

#### BF16

BF16 is the offline baseline.

It also barely fits on the 8GB RTX 3070:

- peak VRAM: `7232.87 MB`

So BF16 offline is feasible on 8GB, but with little safety margin.

#### INT8

INT8 has three defining properties in the active results:

- much lower drift than NF4
- slightly lower VRAM than BF16
- dramatically slower generation than BF16

The key numeric picture is:

- mean MAE vs BF16: `0.01693`
- p95 MAE vs BF16: `0.04109`
- max abs vs BF16: `2.0`
- mean generation: `28.96s`

So INT8 is numerically stable, but speed is poor in this stack.

#### NF4

NF4 has the most interesting offline profile:

- typical cases are relatively close to BF16
- tail risk is catastrophic

Evidence:

- median MAE vs BF16: `0.02982`
- p95 MAE vs BF16: `0.06818`
- but mean MAE vs BF16 jumps to `0.96360`
- and max abs vs BF16 explodes to `9374.95`

That mismatch between median/p95 and mean is the whole story:

- most NF4 samples are normal enough
- a few rare samples blow up badly enough to dominate the average

### Worst NF4 Failure Case

The strongest single offline artifact is the top NF4 worst case:

- sample index: `8`
- stratum: `s01_00pct`
- instruction: `put the white mug on the left plate and put the yellow and white mug on the right plate`
- MAE: `167.56`
- max abs: `9374.95`

The decoded NF4 action text contains a malformed token sequence:

- `5000400`

This is not ordinary quantization noise.

It is a decoding blow-up, and it is exactly the kind of failure mode that can plausibly explain why NF4 online success collapses on a subset of object tasks even though many other tasks still look good.

## Cross-Artifact Interpretation

### 1. Goal Tasks Are Robust

Across all three modes:

- BF16 goal: `20/20`
- NF4 goal: `19/20`
- INT8 goal: `20/20`

This suggests the selected goal tasks are relatively insensitive to quantization at the level used here.

### 2. Object Tasks Separate The Modes

The object suite is where the quantization story becomes meaningful:

- BF16 object: `19/20`
- NF4 object: `11/20`
- INT8 object: `19/20`

This makes object manipulation the most informative suite in the active benchmark.

### 3. INT8 And BF16 Match Online, But Not Operationally

A naive reading would say:

- BF16 and INT8 are equally good, because both get `58/60`

That is incomplete.

The correct reading is:

- BF16 and INT8 match on online success
- INT8 is much more expensive to run
- offline INT8 is about `4.22x` slower than BF16 (`28.96s / 6.86s`)
- online INT8 is about `3.69x` slower than BF16 in total known runtime

So INT8 is an accuracy-preserving but operationally unattractive choice under the current software stack.

### 4. NF4 Has Better Runtime Than INT8 But Worse Reliability

NF4 sits between BF16 and INT8 operationally:

- much faster than INT8 offline
- likely slower than BF16 online on the measured tasks
- much less reliable than BF16 and INT8 on the object suite

This means the real tradeoff is not:

- BF16 vs NF4 vs INT8 on one simple speed axis

It is:

- BF16: strong accuracy, moderate runtime, tight VRAM fit
- INT8: strong accuracy, poor runtime, modest VRAM gain
- NF4: moderate runtime, modest VRAM gain, risky failure tail

### 5. Offline And Online Evidence Agree

The offline benchmark and online benchmark support the same story:

- INT8 is stable but slow
- NF4 is often acceptable, but not robust enough

The fact that NF4 worst offline cases include object-centric instructions involving basket placement is especially important, because the online collapse is also concentrated in an object basket-placement task:

- `pick_up_the_cream_cheese_and_place_it_in_the_basket`

That is strong cross-axis evidence, not just two unrelated experiments.

## What Is Most Publishable From The Active Tree

The most defensible workshop-paper claims supported by the current artifacts are:

1. A matched 6-task LIBERO online comparison exists for `BF16`, `NF4`, and `INT8`.
2. BF16 and INT8 reach the same aggregate online success: `58/60`.
3. NF4 underperforms mainly because of severe degradation on object manipulation tasks.
4. The offline stress benchmark shows that INT8 is numerically close to BF16, while NF4 exhibits catastrophic tail failures despite looking reasonable on most samples.
5. In this stack, INT8 is not a speed optimization and NF4 is not a safe drop-in replacement for BF16.

The strongest single sentence supported by the full active tree is:

`NF4 is usually close to BF16, but its rare catastrophic action-decoding failures are large enough to cause real online reliability loss on object manipulation, while INT8 preserves behavior but is too slow to be an attractive runtime choice in this software stack.`

## Caveats

1. NF4 online elapsed time is incomplete for three recovered local tasks.
2. Dual-GPU experiment notebooks exist but do not contribute completed benchmark evidence inside `active/`.
3. There is one partial local INT8 full-run log, but it was terminated and should not be reported as a completed benchmark result.
4. Exact text match rate vs BF16 is `0.0` for INT8 and NF4 across the offline benchmark, so textual token equality is not a useful fidelity metric here; numeric action drift is the more meaningful measure.

## Recommendation For Downstream Writeup

If this directory is used as the basis for the paper, the cleanest framing is:

- main online matched benchmark:
  - BF16 vs NF4 vs INT8
  - 6 tasks
  - 10 episodes each
- main mechanistic analysis:
  - 180-sample offline BF16 vs INT8 vs NF4 stress benchmark
- key discussion:
  - INT8 preserves behavior but is too slow
  - NF4 is fast enough to be tempting but has a dangerous reliability tail

That framing is fully supported by the artifacts currently present in `active/`.

## Appendix A: Full Active File Inventory

### `kaggle_bf16`

- `kaggle_bf16/goal/GOAL1.ipynb`
- `kaggle_bf16/goal/GOAL2.ipynb`
- `kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260316_112644.json`
- `kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_job01.log`
- `kaggle_bf16/goal/bf16_final_libero_goal__put_the_bowl_on_the_stove_20260317_030334.json`
- `kaggle_bf16/object/OBJECT1.ipynb`
- `kaggle_bf16/object/Object2.ipynb`
- `kaggle_bf16/object/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260316_124347.json`
- `kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260317_025851.json`
- `kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_job01.log`
- `kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260317_025217.json`
- `kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_job01.log`
- `kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260317_122631.json`
- `kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_job01.log`
- `kaggle_bf16/spatial/spartial1.ipynb`
- `kaggle_bf16/spatial/spartial1_dual_gpu_experiment.ipynb`
- `kaggle_bf16/spatial/spatial2.ipynb`

### `kaggle_int8`

- `kaggle_int8/goal/GOAL1.ipynb`
- `kaggle_int8/goal/GOAL1_part1.ipynb`
- `kaggle_int8/goal/GOAL1_part2.ipynb`
- `kaggle_int8/goal/GOAL2.ipynb`
- `kaggle_int8/goal/GOAL2_part1.ipynb`
- `kaggle_int8/goal/GOAL2_part2.ipynb`
- `kaggle_int8/goal/g1p1.ipynb`
- `kaggle_int8/goal/g1p2.ipynb`
- `kaggle_int8/goal/g2p1.ipynb`
- `kaggle_int8/goal/g2p2.ipynb`
- `kaggle_int8/goal/int8_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260323_112149.json`
- `kaggle_int8/goal/int8_final_libero_goal__put_the_bowl_on_the_stove_20260323_112149.json`
- `kaggle_int8/object/OBJECT1.ipynb`
- `kaggle_int8/object/OBJECT1_part1.ipynb`
- `kaggle_int8/object/OBJECT1_part2.ipynb`
- `kaggle_int8/object/Object2.ipynb`
- `kaggle_int8/object/Object2_part1.ipynb`
- `kaggle_int8/object/Object2_part2.ipynb`
- `kaggle_int8/object/int8_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260328_224152.json`
- `kaggle_int8/object/int8_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260328_224708.json`
- `kaggle_int8/object/local_runs/int8_object2_full_20260323_231046.log`
- `kaggle_int8/object/o1p1.ipynb`
- `kaggle_int8/object/o1p2.ipynb`
- `kaggle_int8/object/o2p1.ipynb`
- `kaggle_int8/object/o2p2.ipynb`
- `kaggle_int8/spatial/int8_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260328_224152.json`
- `kaggle_int8/spatial/int8_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260328_224152.json`
- `kaggle_int8/spatial/s1p1.ipynb`
- `kaggle_int8/spatial/s1p2.ipynb`
- `kaggle_int8/spatial/s2p1.ipynb`
- `kaggle_int8/spatial/s2p2.ipynb`
- `kaggle_int8/spatial/spartial1.ipynb`
- `kaggle_int8/spatial/spartial1_dual_gpu_experiment.ipynb`
- `kaggle_int8/spatial/spartial1_part1.ipynb`
- `kaggle_int8/spatial/spartial1_part2.ipynb`
- `kaggle_int8/spatial/spatial2.ipynb`
- `kaggle_int8/spatial/spatial2_part1.ipynb`
- `kaggle_int8/spatial/spatial2_part2.ipynb`

### `kaggle_nf4`

- `kaggle_nf4/goal/nf4_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260318_113438.json`
- `kaggle_nf4/goal/nf4_final_libero_goal__put_the_bowl_on_the_stove_20260318_120218.json`
- `kaggle_nf4/goal/nf4goal1.ipynb`
- `kaggle_nf4/goal/nf4goal2.ipynb`
- `kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.json`
- `kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.log`
- `kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.json`
- `kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.log`
- `kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.json`
- `kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.log`
- `kaggle_nf4/object/nf4_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260318_113830.json`
- `kaggle_nf4/object/nf4_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_localcopy.json`
- `kaggle_nf4/object/nf4object1.ipynb`
- `kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_localcopy.json`
- `kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_localcopy.json`

### `offline_test`

- `offline_test/README.md`
- `offline_test/__pycache__/run_vla0_offline_stress_benchmark.cpython-312.pyc`
- `offline_test/raw/offline_stress_s01_00pct_bf16_int8_nf4_30samples_20260323_112236.json`
- `offline_test/raw/offline_stress_s01_00pct_bf16_int8_nf4_30samples_20260323_112236.log`
- `offline_test/raw/offline_stress_s02_20pct_bf16_int8_nf4_30samples_20260323_114913.json`
- `offline_test/raw/offline_stress_s02_20pct_bf16_int8_nf4_30samples_20260323_114913.log`
- `offline_test/raw/offline_stress_s03_40pct_bf16_int8_nf4_30samples_20260323_124358.json`
- `offline_test/raw/offline_stress_s03_40pct_bf16_int8_nf4_30samples_20260323_124358.log`
- `offline_test/raw/offline_stress_s04_60pct_bf16_int8_nf4_30samples_20260323_135152.json`
- `offline_test/raw/offline_stress_s04_60pct_bf16_int8_nf4_30samples_20260323_135152.log`
- `offline_test/raw/offline_stress_s05_80pct_bf16_int8_nf4_30samples_20260323_152622.json`
- `offline_test/raw/offline_stress_s05_80pct_bf16_int8_nf4_30samples_20260323_152622.log`
- `offline_test/raw/offline_stress_s06_100pct_bf16_int8_nf4_30samples_20260323_174428.json`
- `offline_test/raw/offline_stress_s06_100pct_bf16_int8_nf4_30samples_20260323_174428.log`
- `offline_test/reports/offline_stress_benchmark_brief_20260323.md`
- `offline_test/reports/offline_stress_bf16_int8_nf4_6x30_20260323_112236.json`
- `offline_test/run_vla0_offline_stress_benchmark.py`
