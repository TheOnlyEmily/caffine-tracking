from operator import eq
from caff_data import get_caff_data

if eq(__name__, "__main__"):
    caff_data = get_caff_data()
    print(caff_data)
