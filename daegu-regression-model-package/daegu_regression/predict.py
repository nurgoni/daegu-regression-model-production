from typing import Any, Dict, Union

import numpy as np
import pandas as pd

from daegu_regression import __version__ as _version
from daegu_regression.config.core import app_config, model_config
from daegu_regression.processing.data_manager import load_pipeline
from daegu_regression.processing.validation import validated_inputs

pipeline_file_name = f"{app_config.pipeline_save_file}{_version}.pkl"
_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: Union[pd.DataFrame, Dict]
) -> Dict[str, Any]:

    data = pd.DataFrame(input_data)
    validated_data, errors = validated_inputs(input_data=data)
    results = {
        "predictions": None, "version": _version, "errors": errors
        }

    if not errors:
        predictions = _pipe.predict(
            X=validated_data[model_config.features]
        )
        results = {
            "predictions": [np.exp(pred) for pred in predictions],
            # "predictions": np.exp(predictions),
            "version": _version,
            "errors": errors
        }

    return results
