import streamlit as st


def search_data(search_text, loaded_file_options):
    results = []
    no_results_files = []

    for data, file_name in loaded_file_options:
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

    if results:
        for matched_rows, file_name in results:
            st.write(f"在 {file_name} 表格文件中搜到结果：")
            st.dataframe(matched_rows)

    for file_name in no_results_files:
        st.write(f"在 {file_name} 表格文件中没有搜到匹配的记录。")
