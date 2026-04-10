# Cumulative Benchmark Result Report

Generated from `research/results/active`. GPU model details are intentionally omitted; this document focuses on the recorded benchmark/result-report artifacts.

## Inventory

- Total files scanned: 87
- JSON result reports: 28
- Notebook files: 41
- Notebook files with embedded result reports: 19
- Log files: 14

## Authoritative / Recovered Result Summary

BF16 and NF4 notebook outputs are kept later in the document as mirrors of the saved results, but the table below avoids double-counting them. INT8 now has merged JSON files reconstructed from saved split notebook reports for goal, object, and spatial tasks where completed notebook outputs exist.

| Precision | Kind | Suite | Task | Status | Success | Failure | Time | Source |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| BF16 | goal | libero_goal | open_the_middle_drawer_of_the_cabinet | success | 10 | 0 | 4h 32m 58s | `research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260316_112644.json` |
| BF16 | goal | libero_goal | put_the_bowl_on_the_stove | success | 10 | 0 | 3h 7m 22s | `research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__put_the_bowl_on_the_stove_20260317_030334.json` |
| BF16 | object | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | success | 9 | 1 | 6h 29m 0s | `research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260316_124347.json` |
| BF16 | object | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | success | 10 | 0 | 4h 35m 33s | `research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260317_025851.json` |
| BF16 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | success | 9 | 1 | 3h 41m 28s | `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260317_025217.json` |
| BF16 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | success | 10 | 0 | 3h 43m 23s | `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260317_122631.json` |
| NF4 | goal | libero_goal | open_the_middle_drawer_of_the_cabinet | success | 9 | 1 | 8h 42m 56s | `research/results/active/kaggle_nf4/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260318_113438.json` |
| NF4 | goal | libero_goal | put_the_bowl_on_the_stove | success | 10 | 0 | 5h 0m 39s | `research/results/active/kaggle_nf4/goal/bf16_final_libero_goal__put_the_bowl_on_the_stove_20260318_120218.json` |
| NF4 | object | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | success | 8 | 2 | 11h 18m 19s | `research/results/active/kaggle_nf4/object/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260318_113830.json` |
| NF4 | object | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | success | n/a | n/a | 8h 22m 54s | `research/results/active/kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.json` |
| NF4 | object | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | success | 3 | 7 | n/a | `research/results/active/kaggle_nf4/object/nf4_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_localcopy.json` |
| NF4 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | success | n/a | n/a | 3h 22m 55s | `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.json` |
| NF4 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | success | 9 | 1 | n/a | `research/results/active/kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_localcopy.json` |
| NF4 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | success | n/a | n/a | 3h 23m 5s | `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.json` |
| NF4 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | success | 10 | 0 | n/a | `research/results/active/kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_localcopy.json` |
| INT8 | goal | libero_goal | open_the_middle_drawer_of_the_cabinet | success | 10 | 0 | 17h 26m 30s | `research/results/active/kaggle_int8/goal/int8_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260323_112149.json` |
| INT8 | goal | libero_goal | put_the_bowl_on_the_stove | success | 10 | 0 | 11h 42m 54s | `research/results/active/kaggle_int8/goal/int8_final_libero_goal__put_the_bowl_on_the_stove_20260323_112149.json` |
| INT8 | object | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | success | 10 | 0 | 19h 36m 42s | `research/results/active/kaggle_int8/object/int8_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260328_224152.json` |
| INT8 | object | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | success | 9 | 1 | 19h 14m 6s | `research/results/active/kaggle_int8/object/int8_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260328_224708.json` |
| INT8 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | success | 9 | 1 | 14h 13m 18s | `research/results/active/kaggle_int8/spatial/int8_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260328_224152.json` |
| INT8 | spatial | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | success | 10 | 0 | 14h 16m 12s | `research/results/active/kaggle_int8/spatial/int8_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260328_224152.json` |

## Caveats

- NF4 contains several filenames that still begin with `bf16_final_...`; the internal mode/result content identifies them as NF4.
- NF4 local online probe JSON files do not carry success/failure totals; use the matching `.log` files alongside them.
- INT8 now has merged JSON files for `g1p1 + g1p2`, `g2p1 + g2p2`, `o1p1 + o1p2`, `o2p1 + o2p2`, `s1p1 + s1p2`, and `s2p1 + s2p2`.
- INT8 still does not have saved output-based merged JSONs for every notebook template in the tree; only completed notebook pairs were materialized into JSON.

## BF16

All BF16 structured results are saved as JSON. The notebook outputs in this section mirror those JSON files, plus one notebook without preserved output.

### Structured Result Files

#### research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260316_112644.json

- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-16T11:26:44
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 4h 32m 58s
- Corresponding log files in this tree: `research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_job01.log`

```json
{
  "created_at": "2026-03-16T11:26:44",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 16378.312274217606,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_goal/open_the_middle_drawer_of_the_cabinet/results.json",
      "success": 10,
      "failure": 0,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_goal: 1.000 (10/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 1.000\nTotal success rate: 10/10 (1.000)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial   | libero_object   | libero_goal              | libero_10   | OVERALL        \n----------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | N/A              | N/A             | 100.0 (10/10, 1 tasks)   | N/A         | 100.0 (10/10)  "
  }
}
```

#### research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__put_the_bowl_on_the_stove_20260317_030334.json

- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-17T03:03:34
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 3h 7m 22s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-17T03:03:34",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 11242.357895851135,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_goal/put_the_bowl_on_the_stove/results.json",
      "success": 10,
      "failure": 0,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_goal__put_the_bowl_on_the_stove_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_goal: 1.000 (10/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 1.000\nTotal success rate: 10/10 (1.000)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial   | libero_object   | libero_goal              | libero_10   | OVERALL        \n----------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | N/A              | N/A             | 100.0 (10/10, 1 tasks)   | N/A         | 100.0 (10/10)  "
  }
}
```

#### research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260316_124347.json

- Kind: object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-16T12:43:47
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 9 / 1
- Elapsed: 6h 29m 0s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-16T12:43:47",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_alphabet_soup_and_place_it_in_the_basket"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 23340.327637195587,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_object/pick_up_the_alphabet_soup_and_place_it_in_the_basket/results.json",
      "success": 9,
      "failure": 1,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_object: 0.900 (9/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 0.900\nTotal success rate: 9/10 (0.900)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial   | libero_object          | libero_goal   | libero_10   | OVERALL      \n----------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | N/A              | 90.0 (9/10, 1 tasks)   | N/A           | N/A         | 90.0 (9/10)  "
  }
}
```

#### research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260317_025851.json

- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-17T02:58:51
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 4h 35m 33s
- Corresponding log files in this tree: `research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_job01.log`

```json
{
  "created_at": "2026-03-17T02:58:51",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_cream_cheese_and_place_it_in_the_basket"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_cream_cheese_and_place_it_in_the_basket",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 16533.455248355865,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_object/pick_up_the_cream_cheese_and_place_it_in_the_basket/results.json",
      "success": 10,
      "failure": 0,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_object: 1.000 (10/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 1.000\nTotal success rate: 10/10 (1.000)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial   | libero_object            | libero_goal   | libero_10   | OVERALL        \n--------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | N/A              | 100.0 (10/10, 1 tasks)   | N/A           | N/A         | 100.0 (10/10)  "
  }
}
```

#### research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260317_025217.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-17T02:52:17
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 9 / 1
- Elapsed: 3h 41m 28s
- Corresponding log files in this tree: `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_job01.log`

```json
{
  "created_at": "2026-03-17T02:52:17",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 13287.69650554657,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate/results.json",
      "success": 9,
      "failure": 1,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_spatial: 0.900 (9/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 0.900\nTotal success rate: 9/10 (0.900)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial         | libero_object   | libero_goal   | libero_10   | OVERALL      \n---------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | 90.0 (9/10, 1 tasks)   | N/A             | N/A           | N/A         | 90.0 (9/10)  "
  }
}
```

#### research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260317_122631.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-17T12:26:31
- Modes: bf16
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 3h 43m 23s
- Corresponding log files in this tree: `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_job01.log`

```json
{
  "created_at": "2026-03-17T12:26:31",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "bf16"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "bf16",
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 13402.672304153442,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate/results.json",
      "success": 10,
      "failure": 0,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_spatial: 1.000 (10/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 1.000\nTotal success rate: 10/10 (1.000)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                               | libero_spatial           | libero_object   | libero_goal   | libero_10   | OVERALL        \n-------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_ah_1_ens_pred_8_eval_libero   | 100.0 (10/10, 1 tasks)   | N/A             | N/A           | N/A         | 100.0 (10/10)  "
  }
}
```

### Notebook Files With Saved Result Output

#### research/results/active/kaggle_bf16/goal/GOAL1.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-16T11:26:44
- Episodes per task: 10
- Success / Failure: 10 / 0
- Time: 273.0m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_goal :: open_the_middle_drawer_of_the_cabinet
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260316_112644.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-16T11:26:44
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        open_the_middle_drawer_of_the_cabinet                      10        0     273.0m
Parse step: success
```

#### research/results/active/kaggle_bf16/goal/GOAL2.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-17T03:03:34
- Episodes per task: 10
- Success / Failure: 10 / 0
- Time: 187.4m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_goal :: put_the_bowl_on_the_stove
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_goal__put_the_bowl_on_the_stove_20260317_030334.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-17T03:03:34
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        put_the_bowl_on_the_stove                                  10        0     187.4m
Parse step: success
```

#### research/results/active/kaggle_bf16/object/OBJECT1.ipynb

- Kind: object
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-16T12:43:47
- Episodes per task: 10
- Success / Failure: 9 / 1
- Time: 389.0m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_object :: pick_up_the_alphabet_soup_and_place_it_in_the_basket
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260316_124347.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-16T12:43:47
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_object      pick_up_the_alphabet_soup_and_place_it_in_the_basket        9        1     389.0m
Parse step: success
```

#### research/results/active/kaggle_bf16/object/Object2.ipynb

- Kind: object
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-17T02:58:51
- Episodes per task: 10
- Success / Failure: 10 / 0
- Time: 275.6m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_object :: pick_up_the_cream_cheese_and_place_it_in_the_basket
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_20260317_025851.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-17T02:58:51
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_object      pick_up_the_cream_cheese_and_place_it_in_the_basket        10        0     275.6m
Parse step: success
```

#### research/results/active/kaggle_bf16/spatial/spartial1.ipynb

- Kind: spatial
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Object
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-17T12:26:31
- Episodes per task: 10
- Success / Failure: 10 / 0
- Time: 223.4m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_spatial :: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_20260317_122631.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-17T12:26:31
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_spatial     pick_up_the_black_bowl_next_to_the_ramekin_and_place       10        0     223.4m
Parse step: success
```

#### research/results/active/kaggle_bf16/spatial/spatial2.ipynb

- Kind: spatial
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_i
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-17T02:52:17
- Episodes per task: 10
- Success / Failure: 9 / 1
- Time: 221.5m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['bf16']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_spatial :: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_20260317_025217.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-17T02:52:17
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_spatial     pick_up_the_black_bowl_next_to_the_plate_and_place_i        9        1     221.5m
Parse step: success
```

### Notebook Inventory

| Notebook | Kind | Output Cells | Embedded Report | Suite | Task | Notes |
| --- | --- | ---: | --- | --- | --- | --- |
| `research/results/active/kaggle_bf16/goal/GOAL1.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_bf16/goal/GOAL2.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_bf16/object/OBJECT1.ipynb` | object | 9 | yes | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | contains saved result report |
| `research/results/active/kaggle_bf16/object/Object2.ipynb` | object | 9 | yes | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | contains saved result report |
| `research/results/active/kaggle_bf16/spatial/spartial1_dual_gpu_experiment.ipynb` | spatial | 0 | no | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_bf16/spatial/spartial1.ipynb` | spatial | 9 | yes | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | contains saved result report |
| `research/results/active/kaggle_bf16/spatial/spatial2.ipynb` | spatial | 9 | yes | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | contains saved result report |

### Notebook Metadata Without Saved Result Output

#### research/results/active/kaggle_bf16/spatial/spartial1_dual_gpu_experiment.ipynb

- Title: VLA-0 Kaggle BF16 Final Benchmark: Object
- Kind: spatial
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

### Log Files

- `research/results/active/kaggle_bf16/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_job01.log`
- `research/results/active/kaggle_bf16/object/bf16_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_job01.log`
- `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_job01.log`
- `research/results/active/kaggle_bf16/spatial/bf16_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_job01.log`

## NF4

NF4 mixes final/recovered JSON summaries and local online probe artifacts. Matching logs are listed where the JSON alone does not include totals.

### Structured Result Files

#### research/results/active/kaggle_nf4/goal/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260318_113438.json

- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-18T11:34:38
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 9 / 1
- Elapsed: 8h 42m 56s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-18T11:34:38",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 31376.42784023285,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_goal/open_the_middle_drawer_of_the_cabinet/results.json",
      "success": 9,
      "failure": 1,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_nf4_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_nf4_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_goal: 0.900 (9/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 0.900\nTotal success rate: 9/10 (0.900)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                                   | libero_spatial   | libero_object   | libero_goal            | libero_10   | OVERALL      \n----------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_nf4_ah_1_ens_pred_8_eval_libero   | N/A              | N/A             | 90.0 (9/10, 1 tasks)   | N/A         | 90.0 (9/10)  "
  }
}
```

#### research/results/active/kaggle_nf4/goal/bf16_final_libero_goal__put_the_bowl_on_the_stove_20260318_120218.json

- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-18T12:02:18
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 5h 0m 39s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-18T12:02:18",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 18038.681878566742,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_goal/put_the_bowl_on_the_stove/results.json",
      "success": 10,
      "failure": 0,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_goal__put_the_bowl_on_the_stove_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_nf4_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_nf4_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_goal: 1.000 (10/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 1.000\nTotal success rate: 10/10 (1.000)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                                   | libero_spatial   | libero_object   | libero_goal              | libero_10   | OVERALL        \n--------------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_nf4_ah_1_ens_pred_8_eval_libero   | N/A              | N/A             | 100.0 (10/10, 1 tasks)   | N/A         | 100.0 (10/10)  "
  }
}
```

#### research/results/active/kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.json

- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Protocol/Outcome: online_probe_viable
- Created: 2026-03-20T14:44:47
- Modes: nf4
- Episodes per task: 1
- Status: success
- Success / Failure: n/a / n/a
- Elapsed: 8h 22m 54s
- Corresponding log files in this tree: `research/results/active/kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.log`

```json
{
  "created_at": "2026-03-20T14:44:47",
  "checkpoint": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "device": "cuda:0",
  "task_suite_name": "libero_object",
  "task_name": "pick_up_the_cream_cheese_and_place_it_in_the_basket",
  "mode": "nf4",
  "episodes": 1,
  "total_init_states": 50,
  "task_id_index": 0,
  "task_id_count": 5,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "num_steps": 0,
  "returncode": 0,
  "elapsed_seconds": 30174.424218031985,
  "status": "success",
  "probe_outcome": "online_probe_viable",
  "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_object/pick_up_the_cream_cheese_and_place_it_in_the_basket/results.json",
  "success": null,
  "failure": null,
  "log_path": "/home/proxi/projects/VLA/vla0/research/results/active/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.log",
  "last_log_line": "Evaluation complete."
}
```

#### research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Protocol/Outcome: online_probe_viable
- Created: 2026-03-20T02:58:03
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: n/a / n/a
- Elapsed: 3h 22m 55s
- Corresponding log files in this tree: `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.log`, `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.log`

```json
{
  "created_at": "2026-03-20T02:58:03",
  "checkpoint": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "device": "cuda:0",
  "task_suite_name": "libero_spatial",
  "task_name": "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate",
  "mode": "nf4",
  "episodes": 10,
  "total_init_states": 50,
  "task_id_index": 0,
  "task_id_count": 5,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "num_steps": 0,
  "returncode": 0,
  "elapsed_seconds": 12175.414442789013,
  "status": "success",
  "probe_outcome": "online_probe_viable",
  "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate/results.json",
  "success": null,
  "failure": null,
  "log_path": "/home/proxi/projects/VLA/vla0/research/results/active/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.log",
  "last_log_line": "Evaluation complete."
}
```

#### research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Protocol/Outcome: online_probe_viable
- Created: 2026-03-20T06:21:53
- Modes: nf4
- Episodes per task: 1
- Status: success
- Success / Failure: n/a / n/a
- Elapsed: 3h 23m 5s
- Corresponding log files in this tree: `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.log`, `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.log`

```json
{
  "created_at": "2026-03-20T06:21:53",
  "checkpoint": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "device": "cuda:0",
  "task_suite_name": "libero_spatial",
  "task_name": "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate",
  "mode": "nf4",
  "episodes": 1,
  "total_init_states": 50,
  "task_id_index": 0,
  "task_id_count": 5,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "num_steps": 0,
  "returncode": 0,
  "elapsed_seconds": 12184.862027747993,
  "status": "success",
  "probe_outcome": "online_probe_viable",
  "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate/results.json",
  "success": null,
  "failure": null,
  "log_path": "/home/proxi/projects/VLA/vla0/research/results/active/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.log",
  "last_log_line": "Evaluation complete."
}
```

#### research/results/active/kaggle_nf4/object/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260318_113830.json

- Kind: object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Protocol/Outcome: bf16_final_single_task_benchmark
- Created: 2026-03-18T11:38:30
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 8 / 2
- Elapsed: 11h 18m 19s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-18T11:38:30",
  "protocol": "bf16_final_single_task_benchmark",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_alphabet_soup_and_place_it_in_the_basket"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 5,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 40698.86712002754,
      "results_json_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_object/pick_up_the_alphabet_soup_and_place_it_in_the_basket/results.json",
      "success": 8,
      "failure": 2,
      "log_path": "/kaggle/working/vla0/research/results/bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_job01.log",
      "last_log_line": "Evaluation complete."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Parsing libero results from: /kaggle/working/vla0/checkpoints/vla0-libero\nFiltered by pattern 'model_last*': 1 folders match\nFound 1 evaluation folders:\n  - model_last_nf4_ah_1_ens_pred_8_eval_libero\n\n================================================================================\nSUMMARY RESULTS (Each evaluation folder treated independently)\n================================================================================\n\n============================================================\nRESULTS FOR: model_last_nf4_ah_1_ens_pred_8_eval_libero\n============================================================\n\n1. SUITE-LEVEL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nlibero_object: 0.800 (8/10, 1 tasks)\n\nOVERALL. OVERALL RESULTS for model_last_nf4_ah_1_ens_pred_8_eval_libero:\n--------------------------------------------------\nOverall average across 1 suites: 0.800\nTotal success rate: 8/10 (0.800)\n\n\nResults for: /kaggle/working/vla0/checkpoints/vla0-libero\nEvaluation                                   | libero_spatial   | libero_object          | libero_goal   | libero_10   | OVERALL      \n--------------------------------------------------------------------------------------------------------------------------------------\nmodel_last_nf4_ah_1_ens_pred_8_eval_libero   | N/A              | 80.0 (8/10, 1 tasks)   | N/A           | N/A         | 80.0 (8/10)  "
  }
}
```

#### research/results/active/kaggle_nf4/object/nf4_final_libero_object__pick_up_the_cream_cheese_and_place_it_in_the_basket_localcopy.json

- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Protocol/Outcome: nf4_final_single_task_benchmark_recovered_from_local_results
- Created: 2026-03-21T00:00:00
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 3 / 7
- Elapsed: n/a
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-21T00:00:00",
  "protocol": "nf4_final_single_task_benchmark_recovered_from_local_results",
  "model_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_cream_cheese_and_place_it_in_the_basket"
    }
  ],
  "rollout_episodes_per_task": 10,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_object",
      "task_name": "pick_up_the_cream_cheese_and_place_it_in_the_basket",
      "status": "success",
      "returncode": 0,
      "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_object/pick_up_the_cream_cheese_and_place_it_in_the_basket/results.json",
      "success": 3,
      "failure": 7,
      "log_path": null,
      "last_log_line": "(recovered from local results.json)"
    }
  ],
  "parse": null
}
```

#### research/results/active/kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate_localcopy.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Protocol/Outcome: nf4_final_single_task_benchmark_recovered_from_local_results
- Created: 2026-03-21T00:00:00
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 9 / 1
- Elapsed: n/a
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-21T00:00:00",
  "protocol": "nf4_final_single_task_benchmark_recovered_from_local_results",
  "model_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate"
    }
  ],
  "rollout_episodes_per_task": 10,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate",
      "status": "success",
      "returncode": 0,
      "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate/results.json",
      "success": 9,
      "failure": 1,
      "log_path": null,
      "last_log_line": "(recovered from local results.json)"
    }
  ],
  "parse": null
}
```

#### research/results/active/kaggle_nf4/spatial/nf4_final_libero_spatial__pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate_localcopy.json

- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Protocol/Outcome: nf4_final_single_task_benchmark_recovered_from_local_results
- Created: 2026-03-21T00:00:00
- Modes: nf4
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: n/a
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-21T00:00:00",
  "protocol": "nf4_final_single_task_benchmark_recovered_from_local_results",
  "model_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "nf4"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate"
    }
  ],
  "rollout_episodes_per_task": 10,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "nf4",
      "task_suite_name": "libero_spatial",
      "task_name": "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate",
      "status": "success",
      "returncode": 0,
      "results_json_path": "/home/proxi/projects/VLA/vla0/checkpoints/vla0-libero/model_last_nf4_ah_1_ens_pred_8_eval_libero/libero_spatial/pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate/results.json",
      "success": 10,
      "failure": 0,
      "log_path": null,
      "last_log_line": "(recovered from local results.json)"
    }
  ],
  "parse": null
}
```

### Notebook Files With Saved Result Output

#### research/results/active/kaggle_nf4/goal/nf4goal1.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-18T11:34:38
- Episodes per task: 10
- Success / Failure: 9 / 1
- Time: 522.9m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['nf4']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_goal :: open_the_middle_drawer_of_the_cabinet
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260318_113438.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-18T11:34:38
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        open_the_middle_drawer_of_the_cabinet                       9        1     522.9m
Parse step: success
```

#### research/results/active/kaggle_nf4/goal/nf4goal2.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-18T12:02:18
- Episodes per task: 10
- Success / Failure: 10 / 0
- Time: 300.6m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['nf4']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_goal :: put_the_bowl_on_the_stove
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_goal__put_the_bowl_on_the_stove_20260318_120218.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-18T12:02:18
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        put_the_bowl_on_the_stove                                  10        0     300.6m
Parse step: success
```

#### research/results/active/kaggle_nf4/object/nf4object1.ipynb

- Kind: object
- Notebook title: VLA-0 Kaggle BF16 Final Benchmark: Object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Protocol: bf16_final_single_task_benchmark
- Created: 2026-03-18T11:38:30
- Episodes per task: 10
- Success / Failure: 8 / 2
- Time: 678.3m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['nf4']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 10 episodes
   - libero_object :: pick_up_the_alphabet_soup_and_place_it_in_the_basket
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
bf16_final_libero_object__pick_up_the_alphabet_soup_and_place_it_in_the_basket_20260318_113830.json
========================================================================
Protocol: bf16_final_single_task_benchmark
Created: 2026-03-18T11:38:30
GPUs: [0]
Episodes per task: 10
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_object      pick_up_the_alphabet_soup_and_place_it_in_the_basket        8        2     678.3m
Parse step: success
```

### Notebook Inventory

| Notebook | Kind | Output Cells | Embedded Report | Suite | Task | Notes |
| --- | --- | ---: | --- | --- | --- | --- |
| `research/results/active/kaggle_nf4/goal/nf4goal1.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_nf4/goal/nf4goal2.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_nf4/object/nf4object1.ipynb` | object | 9 | yes | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | contains saved result report |

### Log Files

- `research/results/active/kaggle_nf4/local_nf4_online_benchmark/object/local_nf4_rollout_probe_20260320_062153.log`
- `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260319_233507.log`
- `research/results/active/kaggle_nf4/local_nf4_online_benchmark/spatial/local_nf4_rollout_probe_20260320_025848.log`

## INT8

INT8 now has two merged goal JSON files built from the saved split notebook reports. The original four split notebooks are still listed below as source evidence, while the remaining INT8 notebooks are definitions/templates without stored outputs.

### Structured Result Files

#### research/results/active/kaggle_int8/goal/int8_final_libero_goal__open_the_middle_drawer_of_the_cabinet_20260323_112149.json

- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol/Outcome: int8_final_single_task_benchmark_merged_from_split_notebooks
- Created: 2026-03-23T11:21:49+05:30
- Modes: int8
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 17h 26m 30s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-23T11:21:49+05:30",
  "protocol": "int8_final_single_task_benchmark_merged_from_split_notebooks",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "int8"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 10,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "int8",
      "task_suite_name": "libero_goal",
      "task_name": "open_the_middle_drawer_of_the_cabinet",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 62790,
      "results_json_path": null,
      "success": 10,
      "failure": 0,
      "log_path": null,
      "last_log_line": "Merged from split notebook reports."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Merged from split notebook reports for libero_goal/open_the_middle_drawer_of_the_cabinet. Combined result: 10/10 successes across 2 parts."
  },
  "merged_from_parts": [
    {
      "part_index": 1,
      "part_label": "part1",
      "source_notebook": "research/results/active/kaggle_int8/goal/g1p1.ipynb",
      "source_report_filename": "int8_split_part1_libero_goal__open_the_middle_drawer_of_the_cabinet_20260322_030806.json",
      "created_at": "2026-03-22T03:08:06",
      "episodes": 5,
      "success": 5,
      "failure": 0,
      "elapsed_seconds": 29658,
      "task_id_index": 0,
      "task_id_count": 10,
      "parse_step": "success"
    },
    {
      "part_index": 2,
      "part_label": "part2",
      "source_notebook": "research/results/active/kaggle_int8/goal/g1p2.ipynb",
      "source_report_filename": "int8_split_part2_libero_goal__open_the_middle_drawer_of_the_cabinet_20260322_030850.json",
      "created_at": "2026-03-22T03:08:50",
      "episodes": 5,
      "success": 5,
      "failure": 0,
      "elapsed_seconds": 33132,
      "task_id_index": 1,
      "task_id_count": 10,
      "parse_step": "success"
    }
  ]
}
```

#### research/results/active/kaggle_int8/goal/int8_final_libero_goal__put_the_bowl_on_the_stove_20260323_112149.json

- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol/Outcome: int8_final_single_task_benchmark_merged_from_split_notebooks
- Created: 2026-03-23T11:21:49+05:30
- Modes: int8
- Episodes per task: 10
- Status: success
- Success / Failure: 10 / 0
- Elapsed: 11h 42m 54s
- Corresponding log files in this tree: none found

```json
{
  "created_at": "2026-03-23T11:21:49+05:30",
  "protocol": "int8_final_single_task_benchmark_merged_from_split_notebooks",
  "model_path": "/kaggle/working/vla0/checkpoints/vla0-libero/model_last",
  "modes": [
    "int8"
  ],
  "task_specs": [
    {
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove"
    }
  ],
  "rollout_episodes_per_task": 10,
  "offline_sample_count": 50,
  "run_offline_baseline": false,
  "run_rollout_baseline": true,
  "num_steps": 0,
  "start_seed": 7,
  "action_horizon": 1,
  "ensemble_prediction": 8,
  "rollout_task_id_count": 10,
  "available_gpu_ids": [
    0
  ],
  "rollouts": [
    {
      "job_index": 1,
      "gpu_id": 0,
      "mode": "int8",
      "task_suite_name": "libero_goal",
      "task_name": "put_the_bowl_on_the_stove",
      "status": "success",
      "returncode": 0,
      "elapsed_seconds": 42174,
      "results_json_path": null,
      "success": 10,
      "failure": 0,
      "log_path": null,
      "last_log_line": "Merged from split notebook reports."
    }
  ],
  "parse": {
    "status": "success",
    "returncode": 0,
    "tail": "Merged from split notebook reports for libero_goal/put_the_bowl_on_the_stove. Combined result: 10/10 successes across 2 parts."
  },
  "merged_from_parts": [
    {
      "part_index": 1,
      "part_label": "part1",
      "source_notebook": "research/results/active/kaggle_int8/goal/g2p1.ipynb",
      "source_report_filename": "int8_split_part1_libero_goal__put_the_bowl_on_the_stove_20260322_101627.json",
      "created_at": "2026-03-22T10:16:27",
      "episodes": 5,
      "success": 5,
      "failure": 0,
      "elapsed_seconds": 21102,
      "task_id_index": 0,
      "task_id_count": 10,
      "parse_step": "success"
    },
    {
      "part_index": 2,
      "part_label": "part2",
      "source_notebook": "research/results/active/kaggle_int8/goal/g2p2.ipynb",
      "source_report_filename": "int8_split_part2_libero_goal__put_the_bowl_on_the_stove_20260322_031126.json",
      "created_at": "2026-03-22T03:11:26",
      "episodes": 5,
      "success": 5,
      "failure": 0,
      "elapsed_seconds": 21072,
      "task_id_index": 1,
      "task_id_count": 10,
      "parse_step": "success"
    }
  ]
}
```

### Notebook Files With Saved Result Output

#### research/results/active/kaggle_int8/goal/g1p1.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol: int8_split_single_task_benchmark
- Created: 2026-03-22T03:08:06
- Episodes per task: 5
- Success / Failure: 5 / 0
- Time: 494.3m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['int8']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 5 episodes
   - libero_goal :: open_the_middle_drawer_of_the_cabinet
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
int8_split_part1_libero_goal__open_the_middle_drawer_of_the_cabinet_20260322_030806.json
========================================================================
Protocol: int8_split_single_task_benchmark
Created: 2026-03-22T03:08:06
GPUs: [0]
Episodes per task: 5
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        open_the_middle_drawer_of_the_cabinet                       5        0     494.3m
Parse step: success
```

#### research/results/active/kaggle_int8/goal/g1p2.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Protocol: int8_split_single_task_benchmark
- Created: 2026-03-22T03:08:50
- Episodes per task: 5
- Success / Failure: 5 / 0
- Time: 552.2m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['int8']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 5 episodes
   - libero_goal :: open_the_middle_drawer_of_the_cabinet
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
int8_split_part2_libero_goal__open_the_middle_drawer_of_the_cabinet_20260322_030850.json
========================================================================
Protocol: int8_split_single_task_benchmark
Created: 2026-03-22T03:08:50
GPUs: [0]
Episodes per task: 5
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        open_the_middle_drawer_of_the_cabinet                       5        0     552.2m
Parse step: success
```

#### research/results/active/kaggle_int8/goal/g2p1.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol: int8_split_single_task_benchmark
- Created: 2026-03-22T10:16:27
- Episodes per task: 5
- Success / Failure: 5 / 0
- Time: 351.7m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['int8']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 5 episodes
   - libero_goal :: put_the_bowl_on_the_stove
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
int8_split_part1_libero_goal__put_the_bowl_on_the_stove_20260322_101627.json
========================================================================
Protocol: int8_split_single_task_benchmark
Created: 2026-03-22T10:16:27
GPUs: [0]
Episodes per task: 5
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        put_the_bowl_on_the_stove                                   5        0     351.7m
Parse step: success
```

#### research/results/active/kaggle_int8/goal/g2p2.ipynb

- Kind: goal
- Notebook title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Protocol: int8_split_single_task_benchmark
- Created: 2026-03-22T03:11:26
- Episodes per task: 5
- Success / Failure: 5 / 0
- Time: 351.2m
- Parse step: success

```text
Config ready.
  MODEL_PATH: /kaggle/working/vla0/checkpoints/vla0-libero/model_last
  MODES: ['int8']
  ONLINE_GPU_IDS: [0]
  TASKS: 1 task(s) × 5 episodes
   - libero_goal :: put_the_bowl_on_the_stove
  RUN_OFFLINE_BASELINE = False
  RUN_ROLLOUT_BASELINE = True
  CLEAN_START = False
```


```text
========================================================================
int8_split_part2_libero_goal__put_the_bowl_on_the_stove_20260322_031126.json
========================================================================
Protocol: int8_split_single_task_benchmark
Created: 2026-03-22T03:11:26
GPUs: [0]
Episodes per task: 5
Suite              Task                                                  Success  Failure       Time
--------------------------------------------------------------------------------------------------------------
libero_goal        put_the_bowl_on_the_stove                                   5        0     351.2m
Parse step: success
```

### Notebook Inventory

| Notebook | Kind | Output Cells | Embedded Report | Suite | Task | Notes |
| --- | --- | ---: | --- | --- | --- | --- |
| `research/results/active/kaggle_int8/goal/g1p1.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_int8/goal/g1p2.ipynb` | goal | 9 | yes | libero_goal | open_the_middle_drawer_of_the_cabinet | contains saved result report |
| `research/results/active/kaggle_int8/goal/g2p1.ipynb` | goal | 9 | yes | libero_goal | put_the_bowl_on_the_stove | contains saved result report |
| `research/results/active/kaggle_int8/goal/g2p2.ipynb` | goal | 9 | yes | libero_goal | put_the_bowl_on_the_stove | contains saved result report |
| `research/results/active/kaggle_int8/goal/GOAL1_part1.ipynb` | goal | 0 | no | libero_goal | open_the_middle_drawer_of_the_cabinet | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/goal/GOAL1_part2.ipynb` | goal | 0 | no | libero_goal | open_the_middle_drawer_of_the_cabinet | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/goal/GOAL1.ipynb` | goal | 0 | no | libero_goal | open_the_middle_drawer_of_the_cabinet | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/goal/GOAL2_part1.ipynb` | goal | 0 | no | libero_goal | put_the_bowl_on_the_stove | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/goal/GOAL2_part2.ipynb` | goal | 0 | no | libero_goal | put_the_bowl_on_the_stove | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/goal/GOAL2.ipynb` | goal | 0 | no | libero_goal | put_the_bowl_on_the_stove | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/OBJECT1_part1.ipynb` | object | 0 | no | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/OBJECT1_part2.ipynb` | object | 0 | no | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/OBJECT1.ipynb` | object | 0 | no | libero_object | pick_up_the_alphabet_soup_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/Object2_part1.ipynb` | object | 0 | no | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/Object2_part2.ipynb` | object | 0 | no | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/object/Object2.ipynb` | object | 0 | no | libero_object | pick_up_the_cream_cheese_and_place_it_in_the_basket | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spartial1_dual_gpu_experiment.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spartial1_part1.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spartial1_part2.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spartial1.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spatial2_part1.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spatial2_part2.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | configuration/template only; no saved output cells |
| `research/results/active/kaggle_int8/spatial/spatial2.ipynb` | spatial | 0 | no | libero_spatial | pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate | configuration/template only; no saved output cells |

### Notebook Metadata Without Saved Result Output

#### research/results/active/kaggle_int8/goal/GOAL1_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/goal/GOAL1_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/goal/GOAL1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: open_the_middle_drawer_of_the_cabinet
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/goal/GOAL2_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/goal/GOAL2_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/goal/GOAL2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Goal
- Kind: goal
- Suite: libero_goal
- Task: put_the_bowl_on_the_stove
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/OBJECT1_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/OBJECT1_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/OBJECT1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_alphabet_soup_and_place_it_in_the_basket
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/Object2_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/Object2_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/object/Object2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Object
- Kind: object
- Suite: libero_object
- Task: pick_up_the_cream_cheese_and_place_it_in_the_basket
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spartial1_dual_gpu_experiment.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spartial1_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spartial1_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spartial1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spatial2_part1.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spatial2_part2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Episodes (from notebook header): 5
- Saved output cells: 0
- Result report detected: no

#### research/results/active/kaggle_int8/spatial/spatial2.ipynb

- Title: VLA-0 Kaggle INT8 Final Benchmark: Spatial
- Kind: spatial
- Suite: libero_spatial
- Task: pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate
- Episodes (from notebook header): 10
- Saved output cells: 0
- Result report detected: no

## Other Folder: offline_test

This folder is also present under `research/results/active`, but it does not currently contain saved benchmark output files. It contains the offline stress-benchmark scaffold only.

- Folder: `research/results/active/offline_test`
- README: `research/results/active/offline_test/README.md`
- Runner: `research/results/active/offline_test/run_vla0_offline_stress_benchmark.py`
- Bytecode cache: `research/results/active/offline_test/__pycache__/run_vla0_offline_stress_benchmark.cpython-312.pyc`
- Declared output directories: `research/results/active/offline_test/raw`, `research/results/active/offline_test/reports`
- Saved result files currently present in those output directories: none

The README describes an offline quantization stress benchmark over `bf16`, `int8`, and `nf4`, but no generated raw JSON or aggregated report artifacts are currently stored in this tree.
