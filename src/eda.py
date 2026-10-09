import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


logger = logging.getLogger(__name__)


class EDAAnalyzer:
   

    def __init__(self, figures_dir: Path):
        self.figures_dir = figures_dir
        self.figures_dir.mkdir(parents=True, exist_ok=True)

    def basic_info(self, df: pd.DataFrame) -> None:
              
        
        print("\nПервые 5 строк:")
        print(df.head())

        print("\nРазмер датасета:")
        print(df.shape)

        print("\nТипы данных:")
        print(df.dtypes)

        print("\nПропущенные значения:")
        print(df.isnull().sum())

        print("\nСтатистика по числовым признакам:")
        print(df.describe())

    def plot_burnout_distribution(self, df: pd.DataFrame) -> None:
        
                
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x="Burnout_Risk_Level")
        plt.title("Распределение уровней риска выгорания")
        plt.xlabel("Уровень риска выгорания")
        plt.ylabel("Количество студентов")
        plt.tight_layout()

        path = self.figures_dir / "burnout_distribution.png"
        plt.savefig(path)
        plt.close()

        logger.info(f"График сохранён: {path}")

    def plot_genai_hours_vs_burnout(self, df: pd.DataFrame) -> None:
        
                
        plt.figure(figsize=(9, 5))
        sns.boxplot(data=df, x="Burnout_Risk_Level", y="Weekly_GenAI_Hours")
        plt.title("Связь часов использования GenAI и риска выгорания")
        plt.xlabel("Уровень риска выгорания")
        plt.ylabel("Часы использования GenAI в неделю")
        plt.tight_layout()

        path = self.figures_dir / "genai_hours_vs_burnout.png"
        plt.savefig(path)
        plt.close()

        logger.info(f"График сохранён: {path}")

    def plot_ai_dependency_vs_burnout(self, df: pd.DataFrame) -> None:
        
              
        plt.figure(figsize=(9, 5))
        sns.boxplot(data=df, x="Burnout_Risk_Level", y="Perceived_AI_Dependency")
        plt.title("Связь зависимости от ИИ и риска выгорания")
        plt.xlabel("Уровень риска выгорания")
        plt.ylabel("Оценка зависимости от ИИ")
        plt.tight_layout()

        path = self.figures_dir / "ai_dependency_vs_burnout.png"
        plt.savefig(path)
        plt.close()

        logger.info(f"График сохранён: {path}")

    def plot_correlation_heatmap(self, df: pd.DataFrame) -> None:
              
        
        numeric_df = df.select_dtypes(include=["int64", "float64", "bool"])

        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Корреляционная матрица числовых признаков")
        plt.tight_layout()

        path = self.figures_dir / "correlation_heatmap.png"
        plt.savefig(path)
        plt.close()

        logger.info(f"График сохранён: {path}")

    def run_full_eda(self, df: pd.DataFrame) -> None:
                
        logger.info("Запуск EDA")

        self.basic_info(df)
        self.plot_burnout_distribution(df)
        self.plot_genai_hours_vs_burnout(df)
        self.plot_ai_dependency_vs_burnout(df)
        self.plot_correlation_heatmap(df)

        logger.info("EDA завершён")