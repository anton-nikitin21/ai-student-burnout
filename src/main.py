import logging

from src.config import DATA_PATH, MODELS_DIR, REPORTS_DIR, FIGURES_DIR
from src.data_loader import DataLoader
from src.eda import EDAAnalyzer
from src.preprocessing import DataPreprocessor
from src.trainer import (
    ModelTrainer,
    LogisticRegressionStrategy,
    RandomForestStrategy,
)
from src.evaluator import ModelEvaluator
from src.saver import ResultSaver


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


def main():

    loader = DataLoader(DATA_PATH)
    df = loader.load_data()


    eda = EDAAnalyzer(FIGURES_DIR)
    eda.run_full_eda(df)


    preprocessor = DataPreprocessor()
    X_train, X_test, y_train, y_test, sklearn_preprocessor = preprocessor.prepare_data(df)


    logistic_trainer = ModelTrainer(LogisticRegressionStrategy())
    logistic_model = logistic_trainer.train_model(
        sklearn_preprocessor,
        X_train,
        y_train,
    )


    random_forest_trainer = ModelTrainer(RandomForestStrategy())
    random_forest_model = random_forest_trainer.train_model(
        sklearn_preprocessor,
        X_train,
        y_train,
    )

    
    evaluator = ModelEvaluator(preprocessor.label_encoder)

    logistic_results = evaluator.evaluate(
        logistic_model,
        X_test,
        y_test,
        "logistic_regression",
    )

    random_forest_results = evaluator.evaluate(
        random_forest_model,
        X_test,
        y_test,
        "random_forest",
    )

    results = [logistic_results, random_forest_results]

    comparison, best_model_name = evaluator.compare_models(results)

    
    saver = ResultSaver(MODELS_DIR, REPORTS_DIR)

    saver.save_model(logistic_model, "logistic_regression_model.pkl")
    saver.save_model(random_forest_model, "random_forest_model.pkl")
    saver.save_model(preprocessor.label_encoder, "label_encoder.pkl")

    saver.save_json(results, "model_results.json")

    comparison.to_csv(REPORTS_DIR / "model_comparison.csv", index=False)

    print("\nПроект успешно выполнен.")
    print(f"Лучшая модель по F1-macro: {best_model_name}")


if __name__ == "__main__":
    main()