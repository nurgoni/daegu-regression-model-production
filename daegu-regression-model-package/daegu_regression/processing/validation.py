from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from daegu_regression.config.core import model_config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:

    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in model_config.features
        if validated_data[var].isna().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validated_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:

    relevant_data = input_data[model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        MultipleDataInput(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return (validated_data, errors)


class InputSchema(BaseModel):
    HallwayType: Optional[str]
    TimeToSubway: Optional[str]
    SubwayStation: Optional[str]
    N_FacilitiesNearBy_ETC: Optional[int]
    N_FacilitiesNearBy_PublicOffice: Optional[int]
    N_SchoolNearBy_University: Optional[int]
    N_Parkinglot_Basement: Optional[int]
    YearBuilt: Optional[int]
    N_FacilitiesInApt: Optional[int]
    Size_sqf: Optional[int]


class MultipleDataInput(BaseModel):
    inputs: List[InputSchema]
