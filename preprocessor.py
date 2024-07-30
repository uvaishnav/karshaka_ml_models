# preprocessor.py

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder

def log_normal_transform(x):
    return np.log1p(x)

def get_preprocessor():
    numerical_columns = ["Avg_Nitrogen", "Avg_Phosphorous", "Avg_Potassium", "pH", "temperature", "humidity", "rainfall"]
    categorical_columns = ["Crop"]

    num_pipeline = Pipeline(
        steps=[
            ('log_normal', FunctionTransformer(log_normal_transform)),
            ("scaler", StandardScaler())
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            ("one_hot_encoder", OneHotEncoder()),
            ("scaler", StandardScaler(with_mean=False))
        ]
    )

    preprocessor = ColumnTransformer(
        [
            ("num_pipeline", num_pipeline, numerical_columns),
            ("cat_pipelines", cat_pipeline, categorical_columns)
        ]
    )

    return preprocessor
