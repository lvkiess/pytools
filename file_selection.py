import os
from tkinter import filedialog, Tk, messagebox
from tkinter.messagebox import showerror, askquestion

from excel_processing import process_excel


def select_directory():
    directory = filedialog.askdirectory(title="选择目录")
    if directory:
        file_paths = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.xlsx') or file.endswith('.xls'):
                    file_path = os.path.join(root, file)
                    file_paths.append(file_path)
        if file_paths:
            process_excel(file_paths)
    else:
        messagebox.showinfo("提示", "未选择目录")


def select_multiple_files():
    file_paths = filedialog.askopenfilenames(
        title="选择Excel文件",
        filetypes=[("Excel files", "*.xlsx;*.xls")],
        multiple=True
    )
    if file_paths:
        process_excel(file_paths)
    else:
        messagebox.showinfo("提示", "未选择文件")
