# Reproduction

The six notebooks are the end-to-end experiment entry points:

- `MNIST.ipynb`
- `FassionMNIST.ipynb`
- `KMNIST.ipynb`
- `CIFAR.ipynb`
- `TinyImagenet.ipynb`
- `animeface.ipynb`

Create the environment described in `requirements.txt`, set the dataset root in the notebook, and run the cells from top to bottom. The notebooks are committed without execution outputs so the repository stays small and does not expose local paths or environment metadata.

The standard torchvision datasets are downloaded by their loaders. Tiny ImageNet and AnimeFace must be obtained separately under their respective dataset terms. Record the dataset version, hardware, PyTorch version, seed, and evaluation split when reproducing the paper results.
