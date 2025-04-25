from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path

@dataclass(frozen=True)
class DataLoadConfig:
    root_dir: Path
    raw_data_path: Path
    df_data_path: Path


