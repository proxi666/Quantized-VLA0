# VLA-0 Offline Stress Benchmark: Short Summary

Source report:
- [offline_stress_bf16_int8_nf4_6x30_20260323_112236.json](/home/proxi/projects/VLA/vla0/research/results/active/offline_test/reports/offline_stress_bf16_int8_nf4_6x30_20260323_112236.json)

## Protocol

- Model: `VLA-0`
- Modes: `BF16`, `INT8`, `NF4`
- Device: `RTX 3070 8GB`
- Offline benchmark only, no simulator rollouts
- Fixed stress benchmark:
  - `6` dataset strata
  - `30` samples per stratum
  - `180` total samples
- Comparison target:
  - `INT8` and `NF4` measured against `BF16`

## Main Results

- `BF16`
  - `180` samples
  - mean generation time: `6.86s`
  - peak VRAM: `7232.87 MB`

- `INT8`
  - `180` samples
  - mean generation time: `28.96s`
  - mean MAE vs BF16: `0.01693`
  - p95 MAE vs BF16: `0.04109`
  - max abs vs BF16: `2.0`
  - peak VRAM: `6607.99 MB`

- `NF4`
  - `180` samples
  - mean generation time: `10.04s`
  - mean MAE vs BF16: `0.96360`
  - p95 MAE vs BF16: `0.06818`
  - max abs vs BF16: `9374.95`
  - peak VRAM: `6564.76 MB`

## Interpretation

- `BF16` is the reference and fits on the RTX 3070 for offline evaluation, but only with a small VRAM margin.
- `INT8` is much slower than `BF16`, but its action drift is small on average.
- `NF4` is much faster than `INT8` and only moderately slower than `BF16` on most samples.
- But `NF4` has a catastrophic outlier tail:
  - the overall mean drift is dominated by one or a few extreme decoding failures
  - this is why `NF4` has a huge mean MAE while still having a relatively small `p95` MAE

## Short Takeaway

The offline benchmark suggests:

- `INT8` is numerically stable but operationally slow
- `NF4` is operationally attractive, but less reliable because rare catastrophic failures exist
- this makes the main question for the paper:
  - whether the online LIBERO results show the same tradeoff between average efficiency and rare failure modes

## Paste-Ready Version

We ran a fixed offline stress benchmark for VLA-0 on an RTX 3070 8GB, comparing BF16, INT8, and NF4 on the same 180 samples (6 dataset strata × 30 samples). BF16 was the reference and averaged 6.86s generation time with a 7232.87 MB peak VRAM footprint. INT8 averaged 28.96s, with low drift relative to BF16 (mean MAE 0.01693, p95 MAE 0.04109, max absolute difference 2.0), but was much slower. NF4 averaged 10.04s and used 6564.76 MB peak VRAM, making it much faster than INT8 and closer to BF16 in typical cases (p95 MAE 0.06818), but it exhibited catastrophic outlier behavior: its mean MAE rose to 0.96360 and max absolute difference to 9374.95 because one or a few samples produced extreme decoding failures. So the offline result is not simply “NF4 is worse”; it is “NF4 is usually close, but has a dangerous tail of rare large failures,” while INT8 is more stable but much slower.
