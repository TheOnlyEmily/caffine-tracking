import pandas as pd 


def get_caff_data():
    return pd.read_csv("caff_data.csv", index_col=False, parse_dates=["Date"])