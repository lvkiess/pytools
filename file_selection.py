import os
from tkinter import filedialog, Tk
from tkinter.messagebox import showinfo, showerror

def select_file():
    root = Tk()
    root.withdraw()  # 隐藏Tk窗口
    try:
        file_path = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel files", "*.xlsx;*.xls")]
        )
        return file_path
    except Exception as e:
        showerror("错误", "文件选择时发生错误：" + str(e))
        return None