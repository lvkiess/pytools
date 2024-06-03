import os
import traceback
import psutil
from tkinter import messagebox
from tkinter.messagebox import showinfo, showerror

from adjust_excel import adjust_excel_column_width
from count_result import count_result
import pandas as pd


def process_excel(input_files):
    try:
        all_results = pd.DataFrame()
        output_dir = os.path.dirname(input_files[0])

        for input_file in input_files:
            if not check_and_wait_for_file_not_in_use(input_file):
                messagebox.showinfo("提示", "文件占用中，请关闭后重试")
                break

            df = pd.read_excel(input_file, sheet_name=0, engine='openpyxl')

            input_filename = os.path.basename(input_file)

            result_df = count_result(df, input_filename)

            all_results = pd.concat([result_df, all_results])

        output_file = os.path.join(output_dir, '所有测试结果统计.xlsx')

        if check_output_file_exist(output_file) and check_and_wait_for_file_not_in_use(output_file):

            all_results.to_excel(output_file, index=False)

            # print(all_results.to_string(index=False, justify='left', max_colwidth=25))

            adjust_excel_column_width(output_file, 25, '测试用例')

            showinfo("完成", "所有统计结果已保存到文件：" + output_file)
            if messagebox.askyesno("完成", "是否打开统计文件目录？"):
                os.startfile(output_dir)
        else:
            messagebox.showinfo("提示", "用户取消，未生成统计结果")

    except Exception as e:
        traceback.print_exc()
        showerror("错误", "处理Excel文件时发生错误：" + str(e))


def check_output_file_exist(output_file):
    output_file = os.path.abspath(output_file)

    if os.path.exists(output_file):
        response = messagebox.askyesno(
            "文件已存在",
            f"输出文件 '{output_file}' 已存在。继续执行将覆盖该文件。是否继续？"
        )
        return response
    return True  # 如果文件不存在，直接返回True以继续处理


def is_file_in_use_by_excel(file_path):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            # if 'EXCEL' in proc.info['name']:
            if 'EXCEL' in proc.name():
                for open_file in proc.open_files():
                    normalized_path = os.path.normpath(open_file.path)
                    if normalized_path == file_path:
                        return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, OSError):
            continue
    return False


def check_and_wait_for_file_not_in_use(file_path):
    file_path = os.path.abspath(file_path)

    while is_file_in_use_by_excel(file_path):
        continue_response = messagebox.askyesno(
            "文件正在被使用",
            f"文件 '{file_path}' 正在被Excel使用。请关闭Excel后再尝试。是否继续等待？"
        )
        if not continue_response:
            return False
    return True
