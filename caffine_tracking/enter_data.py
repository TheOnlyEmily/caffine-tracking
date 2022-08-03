from operator import eq
from datetime import datetime
from caff_data import validate_caff_units, append_to_data


def get_command_line_args():
    pass


if eq(__name__, "__main__"):
    caff_type, caff_amount, caff_units = get_command_line_args()
    validate_caff_units(caff_units)
    entry_time_stamp = datetime.now()
    append_to_data(entry_time_stamp, caff_type, caff_amount, caff_units)
