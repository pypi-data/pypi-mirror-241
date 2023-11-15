from mlutils.config import DATA_DIR
from typing import Any
from pathlib import Path
import pandas as pd


class MLUtilsDataLoader:
    """Simple class that allows to load specific datasets

    """

    DATASETS = ["covid_flu.csv", "compas-scores-two-years.csv"]

    @staticmethod
    def load(dataset_name: str) -> Any:

        if dataset_name not in MLUtilsDataLoader.DATASETS:
            raise ValueError(f"Dataset {dataset_name} is unknown")

        if dataset_name == "covid_flu.csv":
            return MLUtilsDataLoader.load_covid_flu()

        if dataset_name == "compas-scores-two-years.csv":
            return MLUtilsDataLoader.load_compas_scores_two_years()

    @staticmethod
    def load_covid_flu() -> pd.DataFrame:
        data_path = DATA_DIR / "covid_flu.csv"
        return pd.read_csv(data_path)

    @staticmethod
    def load_compas_scores_two_years() -> pd.DataFrame:
        data_path = DATA_DIR / "compas-scores-two-years.csv"
        return pd.read_csv(data_path)
