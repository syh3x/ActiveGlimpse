"""Small, dependency-light experiment configuration helpers."""

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class ExperimentConfig:
    dataset: str
    data_root: Path = Path("./data")
    data_variant: int | None = None
    seed: int = 42
    batch_size: int = 128
    epochs: int = 500
    learning_rate: float = 1e-3
    embed_dim: int = 128
    budget: int = 7
    grid_size: int = 5
    snapshot_every: int = 5
    output_dir: Path = Path("./outputs")

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ExperimentConfig":
        """Load an experiment configuration from a YAML file."""
        config_path = Path(path)
        values = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        values["data_root"] = Path(values.get("data_root", "./data"))
        values["output_dir"] = Path(values.get("output_dir", "./outputs"))
        allowed = {field.name for field in cls.__dataclass_fields__.values()}
        unknown = set(values) - allowed
        if unknown:
            names = ", ".join(sorted(unknown))
            raise ValueError(f"Unknown configuration fields: {names}")
        return cls(**values)

    @property
    def visible_fraction(self) -> float:
        """Return the fraction of patches observed by the policy budget."""
        return self.budget / (self.grid_size * self.grid_size)
