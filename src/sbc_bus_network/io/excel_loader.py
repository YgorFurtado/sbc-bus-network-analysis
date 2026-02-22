from pathlib import Path

import pandas as pd


def load_routes(excel_path: str | Path, sheet: str, column: str) -> list[str]:
    dataframe = pd.read_excel(excel_path, sheet_name=sheet)
    values = dataframe[column].dropna().astype(str).tolist()
    return values
