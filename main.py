import os
from tkinter import Tk
from tkinter.messagebox import showinfo, showerror
from file_selection import select_file
from excel_processing import process_excel

def main():
    input_file = select_file()

    if input_file:
        process_excel(input_file)
    else:
        showinfo("取消", "未选择文件，操作已取消。")

if __name__ == "__main__":
    main()