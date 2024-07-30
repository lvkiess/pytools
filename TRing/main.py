import os
import streamlit as st
from load_data import load_data_and_add_to_options
from search import search_data


def load_file_paths_from_config(config_path):
    try:
        with open(config_path, "r", encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Tried to open file: {config_path}")
        return []

    file_paths = []
    for line in lines:
        path, index_str = line.strip().split()
        index = int(index_str)
        file_paths.append([path, index])
    return file_paths


config_path = os.path.abspath(".\\config.txt")

file_paths = load_file_paths_from_config(config_path)
# file_paths = [
#     ["D:\\npc_dmg_type.xlsx", 1],
#     ["D:\\npc_impact.xlsx", 1],
#     ["D:\\npc_base.xlsx", 1],
# ]
loaded_file_options = []

for file_path, index in file_paths:
    loaded_file_option = load_data_and_add_to_options(file_path, index - 1)
    if loaded_file_option:
        loaded_file_options.append(loaded_file_option)

st.title("表格数据搜索")
st.write("当前已加载的表格文件包括：")
selected_files = st.multiselect(
    "选择要搜索的表格文件",
    [file[1] for file in loaded_file_options],
    default=[file[1] for file in loaded_file_options],
)

search_text = st.text_input("请输入搜索词，直接点搜索会显示所有加载表格内容")

if st.button("搜索"):
    search_data(search_text, loaded_file_options)
else:
    st.write("请输入搜索词并点击搜索按钮。")
