import numpy as np
from config.core import app_config, model_config
from pipeline import pipe_one
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split


def run_training() -> None:

    data = load_dataset(file_name=app_config.training_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[model_config.features],
        data[model_config.target],
        test_size=model_config.test_size,
        random_state=model_config.random_state
    )

    y_train = np.log(y_train)

    pipe_one.fit(X_train, y_train)

    save_pipeline(pipeline_to_persist=pipe_one)


if __name__ == "__main__":
    run_training()
