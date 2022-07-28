from operator import eq

if eq(__name__, "__main__"):
    caff_data = get_caff_data()
    data_summary = get_data_summary(caff_data)
    print(data_summary)