import pandas as pd
import os


def get_new_caff_df():
    return pd.DataFrame(columns=["Date", "Type", "Amount", "Units"])


def get_current_caff_data():
    return pd.read_csv("caff_data.csv", index_col=False, parse_dates=["Date"])


def caff_data_csv_exists():
    return os.path.exists("caff_data.csv")


def get_caff_data():
    if caff_data_csv_exists():
        return get_current_caff_data()
    else:
        return get_new_caff_df()
