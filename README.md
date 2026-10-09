# Student Burnout — ML & Django

Я разработал ML-пайплайн для классификации риска выгорания студентов: подготовку данных, сравнение Logistic Regression и Random Forest и интерфейс на Django.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
python manage.py migrate
python manage.py runserver
```

## Устройство проекта

Обучение: `src/`. Веб-интерфейс: `predictor/`. Тесты: `tests/`. Для обучения нужен `data/ai_student_impact_dataset.csv`, схема признаков описана в `src/config.py`. До запуска прогнозирования обучите модели. Это учебная классификация, её качество и применимость к реальным людям не установлены.

Я публикую исходный код без локальных паролей, окружений, баз и журналов. Для воспроизведения анализа я указываю необходимые данные и зависимости.

## Автор

Антон Никитин — [anton-nikitin21](https://github.com/anton-nikitin21).
