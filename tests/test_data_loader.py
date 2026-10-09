import pandas as pd
from src.data_loader import DataLoader


def test_data_loader_loads_file(tmp_path):
    test_file = tmp_path / "test.csv"

    test_df = pd.DataFrame(
        {
            "Student_ID": [1, 2],
            "Burnout_Risk_Level": ["Low", "High"],
        }
    )

    test_df.to_csv(test_file, index=False)

    loader = DataLoader(test_file)
    loaded_df = loader.load_data()

    assert not loaded_df.empty
    assert loaded_df.shape[0] == 2