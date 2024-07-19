import pandas as pd
import os


def load_and_display_data(file_path, index):
    data = pd.read_excel(file_path, sheet_name=None)
    if data and data.values():
        sheet_name = list(data.keys())[index]
        return data[sheet_name].astype(str), sheet_name
    else:
        return None, None


def load_data_and_add_to_options(file_path, index):
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]
    data, sheet_name = load_and_display_data(file_path, index)
    if data is not None:
        return (data, f"{file_name_without_ext} - {sheet_name}")
    return None
