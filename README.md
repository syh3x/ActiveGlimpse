<div align="center">

# ActiveGlimpse

### RL-guided sparse image reconstruction

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1%2B-ee4c2c.svg)
![Status](https://img.shields.io/badge/status-under%20review-yellow.svg)

**[Overview](#overview) • [Results](#headline-results) • [Qualitative Results](#qualitative-results) • [Installation](#installation) • [Reproducing](#reproducing-the-experiments) • [Citation](#license--citation)**

</div>

> **Anonymous review copy.** No author names, personal paths, or identifying links are included below. Do not add any until the double-blind review period ends - see [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md).

---

## Overview

ActiveGlimpse reconstructs images from a limited sequence of observed patches. A learned actor-critic policy decides *where to look next*; a transformer scene memory accumulates what's been seen; a decoder reconstructs the full image from those glimpses alone.

<p align="center">
  <img src="results/figures/Architechture.png" alt="ActiveGlimpse architecture" width="820">
</p>

<div align="center">

| | |
|---|---|
| **Datasets** | MNIST · Fashion-MNIST · KMNIST · CIFAR-10 · Tiny ImageNet · AnimeFace |
| **Observation budget** | 7 patches on a 5×5 grid — ≈28% of the image visible |
| **Main metric** | Peak Signal-to-Noise Ratio (PSNR, dB) |
| **Reproducibility** | Output-free notebooks, fixed seed, per-dataset configs |

</div>

---

## Headline Results

<table>
<tr>
<td width="46%" valign="middle">

<img src="results/figures/psnrComparision.png" alt="PSNR comparison across datasets" width="100%">

</td>
<td width="54%" valign="middle">

**The learned policy beats random glimpse selection on every dataset.**

| Dataset | Random init | Learned policy | Δ |
|---|---:|---:|---:|
| MNIST | 13.85 | **25.56** | +11.71 |
| Fashion-MNIST | 16.40 | **24.77** | +8.37 |
| KMNIST | 10.80 | **18.12** | +7.32 |
| CIFAR-10 | 15.68 | **19.82** | +4.14 |
| AnimeFace | 13.97 | **18.56** | +4.59 |
| Tiny ImageNet | 15.04 | **17.50** | +2.46 |

*Gains are largest on structurally simple datasets (MNIST, Fashion-MNIST) and shrink as texture complexity increases — consistent with a policy that is learning to prioritize informative regions rather than reconstructing on brute force alone.*

Raw values: [`results/metrics.json`](results/metrics.json)

</td>
</tr>
</table>

---

## Qualitative Results

**Dataset coverage** - the six datasets span handwriting, clothing, natural objects, and faces:

<p align="center">
  <img src="results/figures/dataset.png" alt="Dataset examples" width="720">
</p>

**Training dynamics** - cumulative reward, PSNR, and total loss over 300 epochs across all six datasets:

<p align="center">
  <img src="results/figures/training_curve.png" alt="Training curves" width="100%">
</p>

**Policy behavior** - glimpse trajectories the policy selects step-by-step, alongside the resulting reconstruction:

<p align="center">
  <img src="results/figures/trajectry.png" alt="Policy trajectory visualization" width="100%">
</p>

---

## Repository Layout

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── configs/                  # Per-dataset experiment settings (yaml)
├── src/                      # Reusable utilities (config schema, metrics)
├── *.ipynb                   # Output-free, per-dataset experiment notebooks
├── results/
│   ├── figures/              # Paper figures (this README)
│   └── metrics.json          # Source numbers behind the results table
├── checkpoints/              # Pointers to externally-hosted model weights
└── docs/                     # Reproduction notes + release checklist
```

---

## Installation

Python 3.10+ recommended. CUDA-enabled PyTorch is recommended for training; CPU is sufficient for inspection.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Standard datasets are fetched automatically via `torchvision`. AnimeFace and Tiny ImageNet require external downloads - see the relevant notebook for paths and terms.

---

## Reproducing the Experiments

Each notebook is a self-contained, top-to-bottom experiment for one dataset:

| Dataset | Notebook |
|---|---|
| MNIST | [`MNIST.ipynb`](MNIST.ipynb) |
| Fashion-MNIST | [`FassionMNIST.ipynb`](FassionMNIST.ipynb) |
| KMNIST | [`KMNIST.ipynb`](KMNIST.ipynb) |
| CIFAR-10 | [`CIFAR.ipynb`](CIFAR.ipynb) |
| Tiny ImageNet | [`TinyImagenet.ipynb`](TinyImagenet.ipynb) |
| AnimeFace | [`animeface.ipynb`](animeface.ipynb) |

Notebooks ship with outputs cleared, so the repository stays small and no local paths or environment metadata leak in. Set the dataset root at the top of the relevant notebook, then run all cells. Per-dataset hyperparameters mirrored in [`configs/`](configs/) for reference.

---

## Model Weights

Checkpoints (~18 MB each) are not committed to Git. See [`checkpoints/README.md`](checkpoints/README.md) for the external hosting plan (Zenodo / Hugging Face Hub) and download links once released.

---

## License & Citation

Released under the [MIT License](LICENSE). See [`CITATION.cff`](CITATION.cff) - citation details will be finalized after the review period.
