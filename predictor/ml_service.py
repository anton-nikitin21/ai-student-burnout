import joblib
import pandas as pd
from pathlib import Path
from django.conf import settings


class BurnoutPredictionService:

    def __init__(self):
        base_dir = Path(settings.BASE_DIR)

        self.model_path = base_dir / "models" / "random_forest_model.pkl"
        self.label_encoder_path = base_dir / "models" / "label_encoder.pkl"

        self.model = joblib.load(self.model_path)
        self.label_encoder = joblib.load(self.label_encoder_path)

    def predict(self, form_data: dict) -> str:
        """
        Получает данные из формы, превращает их в DataFrame
        и возвращает предсказанный класс риска выгорания.
        """

        prepared_data = {
            "Major_Category": form_data["Major_Category"],
            "Year_of_Study": form_data["Year_of_Study"],
            "Pre_Semester_GPA": form_data["Pre_Semester_GPA"],
            "Post_Semester_GPA": form_data["Post_Semester_GPA"],
            "Weekly_GenAI_Hours": form_data["Weekly_GenAI_Hours"],
            "Primary_Use_Case": form_data["Primary_Use_Case"],
            "Prompt_Engineering_Skill": form_data["Prompt_Engineering_Skill"],
            "Tool_Diversity": form_data["Tool_Diversity"],
            "Paid_Subscription": form_data["Paid_Subscription"] == "True",
            "Traditional_Study_Hours": form_data["Traditional_Study_Hours"],
            "Perceived_AI_Dependency": form_data["Perceived_AI_Dependency"],
            "Institutional_Policy": form_data["Institutional_Policy"],
            "Anxiety_Level_During_Exams": form_data["Anxiety_Level_During_Exams"],
            "Skill_Retention_Score": form_data["Skill_Retention_Score"],
        }

        input_df = pd.DataFrame([prepared_data])

        prediction_encoded = self.model.predict(input_df)[0]

        prediction_label = self.label_encoder.inverse_transform([prediction_encoded])[0]

        return prediction_label