import os
import traceback
from tkinter import messagebox

from count_result import count_result
import pandas as pd
from tkinter.messagebox import showinfo, showerror


def process_excel(input_files):
    try:
        all_results = pd.DataFrame()
        output_dir = os.path.dirname(input_files[0])

        for input_file in input_files:
            df = pd.read_excel(input_file, sheet_name=0, engine='openpyxl')

            input_filename = os.path.basename(input_file)

            result_df = count_result(df, input_filename)

            all_results = pd.concat([result_df, all_results])

        output_file = os.path.join(output_dir, '所有测试结果统计.xlsx')

        all_results.to_excel(output_file, index=False)

        print(all_results.to_string(index=False, justify='left', max_colwidth=10))

        showinfo("完成", "所有统计结果已保存到文件：" + output_file)
        # 显示提示框询问是否打开新表格的位置
        if messagebox.askyesno("完成", "是否打开统计文件目录？"):
            # 使用webbrowser打开文件位置
            os.startfile(output_dir)

    except Exception as e:
        traceback.print_exc()
        showerror("错误", "处理Excel文件时发生错误：" + str(e))
