import streamlit as st
import pandas as pd

# F:\pytest> streamlit run show_excel.py


uploaded_file = st.file_uploader('excel文件', type=['xlsx'])

if uploaded_file is None:
    st.stop()


@st.cache_data
def load_data(file):
    print("执行加载数据")
    return pd.read_excel(file, None)


dfs = load_data(uploaded_file)
names = list(dfs.keys())
sheet_selects = st.multiselect('工作表', names, [])

if len(sheet_selects) == 0:
    st.stop()

tabs = st.tabs(sheet_selects)

for tab, name in zip(tabs, sheet_selects):
    with tab:
        df = dfs[name]
        st.dataframe(df)
