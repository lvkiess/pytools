import pandas as pd
import os
import streamlit as st


@st.cache_data
def load_data_and_add_to_options(file_path, index):
    file_name = os.path.basename(file_path)
    file_name_without_ext = os.path.splitext(file_name)[0]

    data = pd.read_excel(file_path, sheet_name=None)
    if data and data.values():
        sheet_name = list(data.keys())[index]
    else:
        sheet_name = ""

    if data is not None:
        return data[sheet_name].astype(str), f"{file_name_without_ext} - {sheet_name}"
    return None
