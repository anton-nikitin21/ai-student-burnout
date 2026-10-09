# Student Burnout — ML & Django

Учебный ML-пайплайн классификации риска выгорания студентов: подготовка данных, сравнение Logistic Regression и Random Forest, Django-интерфейс.

Проект из учебного портфолио Антона Никитина. Исходные наработки сохранены; подготовка документации и публикации выполнена с помощью ИИ.

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

## Состав и ограничения

Обучение: `src/`. Веб-интерфейс: `predictor/`. Тесты: `tests/`. Для обучения нужен `data/ai_student_impact_dataset.csv`, схема признаков описана в `src/config.py`. До запуска прогнозирования обучите модели. Это учебная классификация, её качество и применимость к реальным людям не установлены.

В репозиторий включён исходный код. Локальные пароли, окружения, базы, журналы и частные наборы данных исключены. Результаты и метрики не заявляются без воспроизводимой проверки.
