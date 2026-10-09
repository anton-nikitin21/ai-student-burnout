from django import forms


class StudentPredictionForm(forms.Form):
    Major_Category = forms.ChoiceField(
        label="Направление обучения",
        choices=[
            ("STEM", "STEM"),
            ("Business", "Business"),
            ("Humanities", "Humanities"),
            ("Medical", "Medical"),
            ("Arts", "Arts"),
        ],
    )

    Year_of_Study = forms.ChoiceField(
        label="Курс обучения",
        choices=[
            ("First", "First"),
            ("Second", "Second"),
            ("Third", "Third"),
            ("Fourth", "Fourth"),
            ("Graduate", "Graduate"),
        ],
    )

    Pre_Semester_GPA = forms.FloatField(
        label="GPA до семестра",
        min_value=1.0,
        max_value=4.0,
        initial=3.0,
    )

    Post_Semester_GPA = forms.FloatField(
        label="GPA после семестра",
        min_value=1.0,
        max_value=4.0,
        initial=3.2,
    )

    Weekly_GenAI_Hours = forms.FloatField(
        label="Часов GenAI в неделю",
        min_value=0,
        max_value=40,
        initial=10,
    )

    Primary_Use_Case = forms.ChoiceField(
        label="Основная цель использования ИИ",
        choices=[
            ("Writing", "Writing"),
            ("Summarization", "Summarization"),
            ("Coding", "Coding"),
            ("Brainstorming", "Brainstorming"),
            ("Answer Generation", "Answer Generation"),
        ],
    )

    Prompt_Engineering_Skill = forms.ChoiceField(
        label="Навык промпт-инжиниринга",
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ],
    )

    Tool_Diversity = forms.IntegerField(
        label="Количество разных ИИ-инструментов",
        min_value=1,
        max_value=5,
        initial=2,
    )

    Paid_Subscription = forms.ChoiceField(
        label="Есть платная подписка?",
        choices=[
            (True, "Да"),
            (False, "Нет"),
        ],
    )

    Traditional_Study_Hours = forms.FloatField(
        label="Часов традиционной учёбы в неделю",
        min_value=1,
        max_value=40,
        initial=10,
    )

    Perceived_AI_Dependency = forms.IntegerField(
        label="Зависимость от ИИ от 1 до 10",
        min_value=1,
        max_value=10,
        initial=5,
    )

    Institutional_Policy = forms.ChoiceField(
        label="Политика университета по ИИ",
        choices=[
            ("Allowed", "Allowed"),
            ("Forbidden", "Forbidden"),
            ("Encouraged", "Encouraged"),
        ],
    )

    Anxiety_Level_During_Exams = forms.IntegerField(
        label="Тревожность на экзаменах от 1 до 10",
        min_value=1,
        max_value=10,
        initial=5,
    )

    Skill_Retention_Score = forms.FloatField(
        label="Сохранение навыков от 0 до 100",
        min_value=0,
        max_value=100,
        initial=70,
    )