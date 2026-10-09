from django.shortcuts import render
from .forms import StudentPredictionForm
from .ml_service import BurnoutPredictionService


def predict_burnout(request):
    prediction = None
    explanation = None

    if request.method == "POST":
        form = StudentPredictionForm(request.POST)

        if form.is_valid():
            service = BurnoutPredictionService()
            prediction = service.predict(form.cleaned_data)

            if prediction == "Low":
                explanation = "Низкий риск выгорания. По введённым данным студент находится в относительно устойчивом состоянии."
            elif prediction == "Medium":
                explanation = "Средний риск выгорания. Есть признаки нагрузки, зависимости от ИИ или тревожности, на которые стоит обратить внимание."
            elif prediction == "High":
                explanation = "Высокий риск выгорания. Модель считает, что сочетание признаков похоже на студентов с высоким риском выгорания."
            else:
                explanation = "Модель вернула нестандартный результат."

    else:
        form = StudentPredictionForm()

    return render(
        request,
        "predictor/predict.html",
        {
            "form": form,
            "prediction": prediction,
            "explanation": explanation,
        },
    )

