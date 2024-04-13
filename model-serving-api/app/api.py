from typing import Any

import numpy as np
import pandas as pd

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder

from daegu_regression import __version__ as model_version
from daegu_regression.predict import make_prediction

from app import __version__, schemas
from app.config import settings


api_router = APIRouter()

@api_router.get("/health", response_model=schemas.Health, status_code=status.HTTP_200_OK)
def health() -> dict:

    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()

@api_router.post("/predict", response_model=schemas.PredictionResult, status_code=status.HTTP_200_OK)
async def predict(input_data: schemas.MultipleInputs) -> Any:

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=json.loads(results["errors"])
        )
    
    return results
