# Results

The PNG figures in this directory are lightweight paper artifacts. The original `.pkl` result dumps remain local because they are large binary files and are ignored by Git.

Before publication, export the numeric values used in the paper to `metrics.json` (or a CSV with the same information). Keep one row per dataset and include the evaluation split, number of runs, seed, metric definition, and whether the value is a mean or a single run. Do not publish a chart without its source numbers.

The current values are stored in `metrics.json` using this schema:

```json
{
  "metric": "PSNR (dB)",
  "evaluation_split": "test",
  "seed": 42,
  "datasets": {
    "mnist": {"random_initialization": 13.85, "learned_policy": 25.56}
  }
}
```

The values currently match the labels in the checked-in PSNR comparison figure. Confirm them against the final paper tables before making the repository public.
