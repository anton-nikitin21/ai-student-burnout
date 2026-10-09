import pandas as pd
from src.preprocessing import DataPreprocessor


def test_split_features_target():
    df = pd.DataFrame(
        {
            "Student_ID": [1, 2, 3],
            "Pre_Semester_GPA": [3.0, 3.5, 2.8],
            "Weekly_GenAI_Hours": [5, 10, 15],
            "Tool_Diversity": [1, 2, 3],
            "Traditional_Study_Hours": [10, 8, 6],
            "Perceived_AI_Dependency": [3, 6, 9],
            "Anxiety_Level_During_Exams": [4, 7, 8],
            "Post_Semester_GPA": [3.2, 3.4, 2.9],
            "Skill_Retention_Score": [80, 75, 70],
            "Major_Category": ["STEM", "Business", "Medical"],
            "Year_of_Study": ["First", "Second", "Third"],
            "Primary_Use_Case": ["Writing", "Coding", "Ideas"],
            "Prompt_Engineering_Skill": ["Beginner", "Intermediate", "Advanced"],
            "Paid_Subscription": [True, False, True],
            "Institutional_Policy": ["Allowed", "Forbidden", "Encouraged"],
            "Burnout_Risk_Level": ["Low", "Medium", "High"],
        }
    )

    preprocessor = DataPreprocessor()
    X, y = preprocessor.split_features_target(df)

    assert "Burnout_Risk_Level" not in X.columns
    assert "Student_ID" not in X.columns
    assert len(y) == 3