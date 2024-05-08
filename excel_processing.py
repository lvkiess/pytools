import os
import traceback

import pandas as pd
from tkinter.messagebox import showinfo, showerror


def process_excel(input_file):
    try:
        df = pd.read_excel(input_file, sheet_name=0, engine='openpyxl')

        output_dir = os.path.dirname(input_file)
        input_filename = os.path.basename(input_file)

        result_list = []

        if '测试结果' in df.columns:
            value_counts = df['测试结果'].value_counts()
            total_count = len(df['测试结果'])
            percentages = value_counts / total_count * 100

            result_list.append(pd.DataFrame({
                '测试用例': input_filename,
                '结果': value_counts.index,
                '出现次数': value_counts.values,
                '占比率': percentages.values
            }))
        else:
            result_list.append(pd.DataFrame({
                '测试用例': input_filename,
                '结果': ['不存在结果栏'],
                '出现次数': [None],
                '占比率': [None]
            }))

        result_df = pd.concat(result_list, ignore_index=True)

        output_file = os.path.join(output_dir, '测试结果统计.xlsx')

        result_df.to_excel(output_file, index=False)

        print(result_df.to_string(index=False, justify='left', max_colwidth=10))

        showinfo("完成", "统计结果已保存到文件：" + output_file)

    except Exception as e:
        traceback.print_exc()
        showerror("错误", "处理Excel文件时发生错误：" + str(e))