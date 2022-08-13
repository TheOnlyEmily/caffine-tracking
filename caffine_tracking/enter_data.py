from operator import eq
from datetime import datetime
from caff_data import append_to_data


def validate_caff_units(caff_unit: str) -> bool:
    """
    Determines if units have the correct dimensionality (volume in this case).

    Args:
        caff_unit: A string respresentation of a unit of measurement.

    Returns:
        A boolean value, where True means that caff_unit is volumetric,
        and False if it's not.
    """
    pass


def get_command_line_args() -> tuple[str, int, str]:
    """
    Extracts three arguments from the command line: the caffine source, 
    the amount of the source, and what units the source amount is measured in, 
    respectively. 

    Returns:
        A tuple containing the caffine source name, the amount of the source,
        and the units for measuring the caffine amount. 
    """
    pass


if eq(__name__, "__main__"):
    caff_type, caff_amount, caff_units = get_command_line_args()
    validate_caff_units(caff_units)
    entry_time_stamp = datetime.now()
    append_to_data(entry_time_stamp, caff_type, caff_amount, caff_units)
