from tkinter import filedialog, Tk
from tkinter.messagebox import showerror


def select_file():
    root = Tk()
    root.geometry("1x1")
    root.attributes('-alpha', 0.1)

    try:
        file_paths = filedialog.askopenfilenames(
            title="选择Excel文件",
            filetypes=[("Excel files", "*.xlsx;*.xls")],
            multiple=True
        )
        return file_paths
    except Exception as e:
        showerror("错误", "文件选择时发生错误：" + str(e))
        return None
