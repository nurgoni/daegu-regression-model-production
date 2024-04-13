from pathlib import Path
from typing import Dict, List, Optional

from pydantic import BaseModel
from strictyaml import YAML, load

import daegu_regression

# project directories
PACKAGE_ROOT = Path(daegu_regression.__file__).resolve().parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):

    package_name: str
    training_data_file: str
    test_data_file: str
    pipeline_save_file: str


class ModelConfig(BaseModel):

    target: str
    variables_to_rename: Dict
    features: List[str]
    test_size: float
    random_state: int
    minmax_scaling_vars: List[str]
    standard_scaling_vars: List[str]
    binning_vars: List[str]
    one_hot_vars: List[str]
    n_estimators: int
    min_samples_split: int
    min_samples_leaf: int
    max_features: str
    max_depth: int

# class Config(BaseModel):
#     model_config: ModelConfig
#     app_config: AppConfig


def find_config_file() -> Path:
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    else:
        raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Optional[Path] = None) -> YAML:

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    else:
        raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None):

    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # _config = Config(
    #     app_config=AppConfig(**parsed_config.data),
    #     model_config=ModelConfig(**parsed_config.data)
    # )

    app_config = AppConfig(**parsed_config.data)
    model_config = ModelConfig(**parsed_config.data)

    return app_config, model_config


app_config, model_config = create_and_validate_config()
