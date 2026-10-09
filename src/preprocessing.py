import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

from src.config import (
    TARGET_COLUMN,
    NUMERIC_FEATURES,
    CATEGORICAL_FEATURES,
    TEST_SIZE,
    RANDOM_STATE,
)


logger = logging.getLogger(__name__)


class DataPreprocessor:
    
    #класс для подготовки признаков и целевой переменной
    

    def __init__(self):
        self.label_encoder = LabelEncoder()
        self.preprocessor = None

    def split_features_target(self, df: pd.DataFrame):
        
                
        if TARGET_COLUMN not in df.columns:
            raise ValueError(f"В датасете нет целевой колонки: {TARGET_COLUMN}")

        X = df.drop(columns=[TARGET_COLUMN, "Student_ID"])
        y = df[TARGET_COLUMN]

        return X, y

    def encode_target(self, y):
                    
        
        y_encoded = self.label_encoder.fit_transform(y)
        return y_encoded

    def build_preprocessor(self):
        
                   
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("num", StandardScaler(), NUMERIC_FEATURES),
                ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ]
        )

        return self.preprocessor

    def train_test_split_data(self, X, y):
        
        
        return train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
            stratify=y,
        )

    def prepare_data(self, df: pd.DataFrame):
                     
        logger.info("Начинаем подготовку данных")

        X, y = self.split_features_target(df)
        y_encoded = self.encode_target(y)

        X_train, X_test, y_train, y_test = self.train_test_split_data(X, y_encoded)

        preprocessor = self.build_preprocessor()

        logger.info("Подготовка данных завершена")

        return X_train, X_test, y_train, y_test, preprocessor