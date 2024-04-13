from daegu_regression.config.core import model_config
from daegu_regression.processing.features import YearBinning


def test_year_binning(sample_input_data):

    transformer = YearBinning(variables=model_config.binning_vars)

    assert sample_input_data["YearBuilt"].iat[0] == 2007

    subject = transformer.fit_transform(sample_input_data)

    assert subject["YearBuilt"].iat[0] == "2002-2007"
