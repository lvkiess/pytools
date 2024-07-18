import streamlit as st
from load_data import load_excel
import os


def search_data(selected_files, search_text, loaded_file_options):
    results = []

    for file_path, file_name in loaded_file_options:
        if file_name in selected_files:
            data = load_excel(file_path)
            if data:
                sheet_name = list(data.keys())[0]  # 获取第一个工作表的名称
                data = data[sheet_name].astype(str)
                matched_rows = data[
                    data.apply(
                        lambda x: any(
                            x.str.contains(search_text, case=False, na=False)
                        ),
                        axis=1,
                    )
                ]
                if not matched_rows.empty:
                    results.append(
                        (matched_rows, os.path.basename(file_path), sheet_name)
                    )

    if results:
        for matched_rows, file_path, sheet_name in results:
            file_name_display = os.path.splitext(os.path.basename(file_path))[
                0
            ]  # 移除路径和后缀
            st.write(
                f"在 {file_name_display} 表格文件的 {sheet_name} 工作表里搜到结果："
            )
            st.dataframe(matched_rows)
    else:
        st.write("没有找到匹配的记录。")
