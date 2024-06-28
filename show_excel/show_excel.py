import streamlit as st
import pandas as pd

local_file = "P:\\_TR\\UE5\\TRing\\RawData\\NpcAttackData.xlsx"

local_df = pd.read_excel(local_file, sheet_name=None)
local_sheet_names = list(local_df.keys())

# 直接使用第一个工作表的名称
first_sheet_name = local_sheet_names[1]
st.subheader(f"工作表: {first_sheet_name} - 第一个文件内容")
st.dataframe(local_df[first_sheet_name])


# 上传第一个Excel文件
uploaded_file1 = st.file_uploader('上传第一个excel文件', type=['xlsx'])

# 如果第一个文件未上传，则停止执行
if uploaded_file1 is None:
    st.stop()

# 加载第一个Excel文件的所有工作表
dfs1 = {}
if uploaded_file1:
    dfs1 = pd.read_excel(uploaded_file1, sheet_name=None)
    sheet_names1 = list(dfs1.keys())
    sheet_select1 = st.multiselect('选择第一个文件中的工作表', sheet_names1)

# 如果没有选择任何工作表，显示错误
if not sheet_select1:
    st.error('请至少选择一个工作表！')
    st.stop()

# 显示第一个文件选择的工作表内容
for sheet_name1 in sheet_select1:
    st.subheader(f"工作表: {sheet_name1} - 第一个文件内容")
    st.dataframe(dfs1[sheet_name1])

# 上传第二个Excel文件
uploaded_file2 = st.file_uploader('上传第二个excel文件', type=['xlsx'])

# 如果第二个文件未上传，则停止执行
if uploaded_file2 is None:
    st.stop()

# 加载第二个Excel文件的所有工作表
dfs2 = {}
if uploaded_file2:
    dfs2 = pd.read_excel(uploaded_file2, sheet_name=None)
    sheet_names2 = list(dfs2.keys())
    sheet_select2 = st.multiselect('选择第二个文件中的工作表', sheet_names2)

# 如果没有选择任何工作表，显示错误
if not sheet_select2:
    st.error('请至少选择一个工作表！')
    st.stop()

# 显示第二个文件选择的工作表内容
for sheet_name2 in sheet_select2:
    st.subheader(f"工作表: {sheet_name2} - 第二个文件内容")
    st.dataframe(dfs2[sheet_name2])

# 假设第二个文件的工作表至少有三列
df2 = dfs2[sheet_name2]
if df2.shape[1] < 3:
    st.error('第二个文件的工作表必须至少有三列！')
    st.stop()

search_column2 = df2.iloc[:, 0]  # 第二个文件的第一列用于搜索
data_column2 = df2.iloc[:, 2]  # 第二个文件的第三列包含要显示的数据


def search_and_display(search_text, dfs1, dfs2, search_column2, data_column2):
    found_matches = []

    # 获取第一个文件选定的工作表名称
    first_file_selected_sheet_name = sheet_select1[0]  # 假设只选择了第一个文件的一个工作表

    # 获取第一个文件选定工作表的数据
    df1 = dfs1[first_file_selected_sheet_name]

    # 显示第一个文件选定工作表的第一列内容
    st.subheader(f'第一个文件 {first_file_selected_sheet_name} 第一列内容')
    st.write(df1[df1.columns[0]])

    # 搜索匹配项
    matched_rows = df1[df1.columns[0]].astype(str) == search_text
    if matched_rows.any():
        st.subheader(f'在 {first_file_selected_sheet_name} 工作表中找到匹配的搜索结果')
        st.write(df1[matched_rows])

        # 遍历第二个文件中选定的所有工作表
        for sheet_name in sheet_select2:
            # 获取第二个文件选定工作表的数据
            df2 = dfs2[sheet_name]

            # 获取匹配的索引，并找到对应的第三列的值（如果存在）
            for index in matched_rows[matched_rows].index:
                # 尝试获取第二个文件中与第一个文件匹配项相对应的第三列的值
                try:
                    matched_result = \
                        df2[df2.iloc[:, 0] == df1.at[index, df1.columns[0]]].iloc[0, 2]
                    found_matches.append((first_file_selected_sheet_name, search_text, matched_result, sheet_name))
                except (IndexError, KeyError):
                    # 如果找不到匹配项或列，则跳过
                    continue

    # 显示第一个文件需要匹配列的所有内容
    st.subheader(f'第二个文件选定的工作表需要匹配列内容')
    for sheet_name in sheet_select2:
        st.write(f"工作表: {sheet_name}")
        st.write(dfs2[sheet_name].iloc[:, 0])

    return found_matches


# 获取用户输入的搜索ID
search_text = st.text_input('请输入搜索词')
if st.button('搜索'):
    results = search_and_display(search_text, dfs1, dfs2, search_column2, data_column2)

    if results:
        for sheet_name, id_, data, source_sheet in results:
            st.write(f"在{sheet_name}工作表中找到了ID {id_}，对应的数据是：{data}")
    else:
        st.write("没有找到匹配的ID。")