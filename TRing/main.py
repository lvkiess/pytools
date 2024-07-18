import streamlit as st
from load_data import load_and_display_data
from search import search_data
import os


def load_data_and_add_to_options(file_path):
    file_name = os.path.basename(file_path)  # 提取文件名
    file_name_without_ext = os.path.splitext(file_name)[0]  # 移除后缀
    data, stname = load_and_display_data(file_path)
    if data is not None:
        return (file_path, file_name_without_ext)
    return None


st.title("表格数据搜索")

file_paths = [
    "D:\\npc_dmg_type.xlsx",
    "D:\\npc_impact.xlsx",
]  # 这里可以添加更多的文件路径
loaded_files = []
loaded_file_options = []

for file_path in file_paths:
    loaded_file_option = load_data_and_add_to_options(file_path)
    if loaded_file_option:
        loaded_file_options.append(loaded_file_option)

st.write("当前已加载的表格文件包括：")
selected_files = st.multiselect(
    "选择要搜索的表格文件",
    [file[1] for file in loaded_file_options],
    default=[file[1] for file in loaded_file_options],
)

search_text = st.text_input("请输入搜索词")

if st.button("搜索"):
    search_data(selected_files, search_text, loaded_file_options)
else:
    st.write("请输入搜索词并点击搜索按钮。")
