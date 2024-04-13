from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.wrappers import SklearnTransformerWrapper
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from daegu_regression.config.core import model_config
from daegu_regression.processing import features as pp

standard = SklearnTransformerWrapper(
    StandardScaler(),
    model_config.standard_scaling_vars
)

minmax = SklearnTransformerWrapper(
    MinMaxScaler(),
    model_config.minmax_scaling_vars
)

pipe_one = Pipeline([
    ("binning", pp.YearBinning(
        variables=model_config.binning_vars
    )),
    ("minmax_scaling", minmax),
    ("standard_scaling", standard),
    ("rare_label_encoder", RareLabelEncoder(
        tol=0.05,
        n_categories=1,
        variables=model_config.one_hot_vars
    )),
    ("one_hot_encoder", OneHotEncoder(
        drop_last=True,
        variables=model_config.one_hot_vars
    )),
    ("predictor", RandomForestRegressor(
        n_estimators=model_config.n_estimators,
        min_samples_split=model_config.min_samples_split,
        min_samples_leaf=model_config.min_samples_leaf,
        max_features=model_config.max_features,
        max_depth=model_config.max_depth
    ))
])
