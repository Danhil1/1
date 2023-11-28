import pandas as pd
import pickle
from src.constants import STAR_NAME, NOT_P_STAR_NAME, STAR_LABEL
from sklearn.pipeline import Pipeline
from src.data_model import PredictionRow


class PredictionModel:
    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file, "rb") as f:
            self.model: Pipeline = pickle.load(f)

    def predict(self, data_model: PredictionRow) -> str:
        if type(data_model) is list and len(data_model) > 0:
            data_model = data_model[0]
        prdct_row = data_model.dict()
        series = pd.Series(prdct_row)
        df = pd.DataFrame(data=[series])
        prediction = self.model.predict(df)
        return STAR_NAME if prediction[0] == STAR_LABEL else NOT_P_STAR_NAME
