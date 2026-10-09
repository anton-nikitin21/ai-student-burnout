import logging

from sklearn.pipeline import Pipeline

from src.model_factory import ModelFactory


logger = logging.getLogger(__name__)


class TrainingStrategy:

    def train(self, preprocessor, X_train, y_train):
        raise NotImplementedError("Метод train должен быть реализован в дочернем классе")


class LogisticRegressionStrategy(TrainingStrategy):

    def train(self, preprocessor, X_train, y_train):
        model = ModelFactory.create_model("logistic_regression")

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        pipeline.fit(X_train, y_train)

        return pipeline


class RandomForestStrategy(TrainingStrategy):

    def train(self, preprocessor, X_train, y_train):
        model = ModelFactory.create_model("random_forest")

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        pipeline.fit(X_train, y_train)

        return pipeline


class ModelTrainer:

    def __init__(self, strategy: TrainingStrategy):
        self.strategy = strategy

    def train_model(self, preprocessor, X_train, y_train):
        logger.info("Начинаем обучение модели")
        model = self.strategy.train(preprocessor, X_train, y_train)
        logger.info("Обучение модели завершено")
        return model