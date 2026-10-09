from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


class ModelFactory:  

    @staticmethod
    def create_model(model_name: str):
        if model_name == "logistic_regression":
            return LogisticRegression(
                max_iter=1000,
                random_state=42,
                class_weight="balanced",
            )

        if model_name == "random_forest":
            return RandomForestClassifier(
                n_estimators=150,
                random_state=42,
                class_weight="balanced",
            )

        raise ValueError(f"Неизвестная модель: {model_name}")