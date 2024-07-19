import os

import streamlit as st
from load_data import load_excel


def search_data(selected_files, search_text, loaded_file_options):
    results = []
    no_results_files = []

    for file_path, file_name in loaded_file_options:
        data = load_excel(file_path)
        if data and data.values():  # 检查字典是否非空
            sheet_name = list(data.keys())[0]
            data = data[sheet_name].astype(str)
            matched_rows = data[
                data.apply(
                    lambda x: any(x.str.contains(search_text, case=False, na=False)),
                    axis=1,
                )
            ]
            if not matched_rows.empty:
                results.append((matched_rows, file_name))
            else:
                no_results_files.append(file_name)
        else:
            no_results_files.append(file_name)

    if results:
        for matched_rows, file_name in results:
            file_name_display = os.path.splitext(file_name)[0]
            st.write(f"在 {file_name_display} 表格文件中搜到结果：")
            st.dataframe(matched_rows)

    for file_name in no_results_files:
        st.write(f"在 {file_name} 表格文件中没有搜到匹配的记录。")
