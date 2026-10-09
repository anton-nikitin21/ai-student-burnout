import logging
import pandas as pd
from pathlib import Path


logger = logging.getLogger(__name__)


class DataLoader:
    
      

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        
                
        try:
            logger.info("Начинаем загрузку данных")

            if not self.file_path.exists():
                raise FileNotFoundError(f"Файл не найден: {self.file_path}")

            df = pd.read_csv(self.file_path)

            if df.empty:
                raise ValueError("Файл загружен, но датасет пустой")

            logger.info("Данные успешно загружены")
            logger.info(f"Размер датасета: {df.shape}")

            return df

        except Exception as error:
            logger.error(f"Ошибка при загрузке данных: {error}")
            raise