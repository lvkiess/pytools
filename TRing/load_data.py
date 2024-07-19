import pandas as pd
import os


def load_excel(file_path):
    return pd.read_excel(file_path, sheet_name=None)


def load_and_display_data(file_path):
    data = load_excel(file_path)
    if data and data.values():  # 检查字典是否非空
        sheet_name = list(data.keys())[0]
        return data[sheet_name].astype(str), sheet_name
    else:
        return None, None


def load_data_and_add_to_options(file_path):
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]
    data, sheet_name = load_and_display_data(file_path)
    if data is not None:
        return (file_path, f"{file_name_without_ext} - {sheet_name}")
    return None
