import json
import logging
import joblib
from pathlib import Path


logger = logging.getLogger(__name__)


class ResultSaver:

    def __init__(self, models_dir: Path, reports_dir: Path):
        self.models_dir = models_dir
        self.reports_dir = reports_dir

        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def save_model(self, model, file_name: str):

        path = self.models_dir / file_name
        joblib.dump(model, path)

        logger.info(f"Модель сохранена: {path}")

    def save_json(self, data, file_name: str):

        path = self.reports_dir / file_name

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        logger.info(f"JSON сохранён: {path}")