import pandas as pd
import os


def get_new_caff_df() -> pd.DataFrame:
    return pd.DataFrame(columns=["Date", "Type", "Amount", "Units"])


def get_current_caff_data() -> pd.DataFrame:
    return pd.read_csv("caff_data.csv", index_col=False, parse_dates=["Date"])


def caff_data_csv_exists() -> bool:
    return os.path.exists("caff_data.csv")


def get_caff_data() -> pd.DataFrame:
    if caff_data_csv_exists():
        return get_current_caff_data()
    else:
        return get_new_caff_df()
