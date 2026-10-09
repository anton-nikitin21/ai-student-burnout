import logging
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


logger = logging.getLogger(__name__)


class ModelEvaluator:

    def __init__(self, label_encoder):
        self.label_encoder = label_encoder

    def evaluate(self, model, X_test, y_test, model_name: str):
    
        logger.info(f"Оцениваем модель: {model_name}")

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        f1_macro = f1_score(y_test, y_pred, average="macro")

        report = classification_report(
            y_test,
            y_pred,
            target_names=self.label_encoder.classes_,
            output_dict=True,
        )

        cm = confusion_matrix(y_test, y_pred)

        print(f"\nМодель: {model_name}")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"F1-macro: {f1_macro:.4f}")

        print("\nClassification report:")
        print(
            classification_report(
                y_test,
                y_pred,
                target_names=self.label_encoder.classes_,
            )
        )

        print("\nConfusion matrix:")
        print(cm)

        return {
            "model_name": model_name,
            "accuracy": accuracy,
            "f1_macro": f1_macro,
            "classification_report": report,
            "confusion_matrix": cm.tolist(),
        }

    def compare_models(self, results):

        comparison = pd.DataFrame(
            [
                {
                    "model": result["model_name"],
                    "accuracy": result["accuracy"],
                    "f1_macro": result["f1_macro"],
                }
                for result in results
            ]
        )

        print("\nСравнение моделей:")
        print(comparison)

        best_model_row = comparison.sort_values(
            by="f1_macro",
            ascending=False,
        ).iloc[0]

        print("\nЛучшая модель:")
        print(best_model_row)

        return comparison, best_model_row["model"]