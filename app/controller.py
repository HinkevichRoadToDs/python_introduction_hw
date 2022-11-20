from ui import get_mode, get_parameter, display_filtered_data, get_newdata, get_changes, get_row_number, get_del_id
from csv_module import filter_data, append_data, change_data, remove_data
from logger import create_log


def start_engine():
    while True:
        mode = get_mode()
        if mode == 0:
            create_log(mode)
            return
        if mode == 1:
            param = get_parameter()
            data = filter_data(True, param)
            display_filtered_data(data)
            create_log(mode, searching=param)
        if mode == 2:
            data = filter_data(False, {})
            display_filtered_data(data)
            create_log(mode)
        if mode == 3:
            dict_new = get_newdata()
            row_numb = append_data(dict_new)
            dict_new.pop('id')
            create_log(mode, row_numb=row_numb, changes=dict_new)
        if mode == 4:
            del_id = get_del_id()
            del_element = remove_data(del_id)
            del_element.pop('id')
            create_log(mode, row_numb=del_id,changes=del_element)
        if mode == 5:
            row_numb = get_row_number()
            what_changed = get_changes()
            change_data(row_numb, what_changed)
            print("Изменения сохранены.")
            create_log(mode, row_numb=row_numb, changes=what_changed)
