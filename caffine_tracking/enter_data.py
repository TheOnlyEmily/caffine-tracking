if __name__ == "__name__":
    caff_type, caff_amount, caff_units = get_comand_line_args()
    validate_caff_units(caff_units)
    entry_time_stamp = get_entry_time_stamp()
    append_to_data(entry_time_stamp, caff_type, caff_amount, caff_units)