from ui import get_mode, get_parameter, display_filtered_data
from csv_module import filter_data


def start_engine():
    mode = get_mode()
    if mode == 1:
        data = filter_data(True, get_parameter())
        display_filtered_data(data)
    if mode == 2:
        data = filter_data(False, {})
        display_filtered_data(data)
