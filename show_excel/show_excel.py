import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader('上传excel文件', type=['xlsx'])

if uploaded_file is None:
    st.stop()


@st.cache_data
def load_data(file):
    print("执行加载数据")
    return pd.read_excel(file, None)


dfs = load_data(uploaded_file)
names = list(dfs.keys())
sheet_selects = st.multiselect('选择工作表', names, [])

if len(sheet_selects) == 0:
    st.stop()

# 初始化搜索文本和搜索结果
search_text = ''
search_results = {}

# 用户输入搜索ID并点击搜索按钮
find = st.text_input('输入搜索内容')
if st.button('搜索'):
    search_text = find
    search_results = {}

    for name in sheet_selects:
        df = dfs[name]
        # 假设我们要搜索的列是第二列（索引为1）
        if 'Unnamed: 0' in df.columns or df.columns[0] in df.columns:  # 确保第二列存在
            column_to_search = 'Unnamed: 0' if 'Unnamed: 0' in df.columns else df.columns[0]
            filtered_df = df[df[column_to_search].astype(str).str.contains(search_text, case=False, na=False)]
            search_results[name] = filtered_df

# 使用tabs显示工作表内容
tabs = st.tabs(sheet_selects)

for tab, name in zip(tabs, sheet_selects):
    with tab:
        if name in search_results and not search_results[name].empty:
            # 显示搜索匹配的内容
            st.subheader(f"工作表: {name} - 搜索结果")
            st.dataframe(search_results[name])
        else:
            # 显示所有内容或没有搜索结果的提示
            if search_text:
                st.subheader(f"工作表: {name} - 没有找到匹配项")
            else:
                df = dfs[name]
                st.dataframe(df)
