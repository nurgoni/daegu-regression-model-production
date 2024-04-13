from pydantic import BaseModel
from typing import Any, List, Optional

from daegu_regression.processing.validation import InputSchema


class PredictionResult(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleInputs(BaseModel):
    inputs: List[InputSchema]

    class Config:
        arbitrary_types_allowed=True
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "HallwayType": "terraced",
                        "TimeToSubway": "0-5min",
                        "SubwayStation": "Kyungbuk_uni_hospital",
                        "N_FacilitiesNearBy_ETC": 0,
                        "N_FacilitiesNearBy_PublicOffice": 3,
                        "N_SchoolNearBy_University": 2,
                        "N_Parkinglot_Basement": 1270,
                        "YearBuilt": 2007, 
                        "N_FacilitiesInApt": 10,
                        "Size_sqf": 1643
                    }
                ]
            }
        }
