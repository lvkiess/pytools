import pandas as pd


def load_excel(file_path):
    return pd.read_excel(file_path, sheet_name=None)


def load_and_display_data(file_path):
    data = load_excel(file_path)
    if data:
        sheet_name = list(data.keys())[0]  # 获取第一个工作表的名称
        return data[sheet_name].astype(str), sheet_name
    else:
        return None, None
