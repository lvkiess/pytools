from tkinter import filedialog, Tk
from tkinter.messagebox import showerror


def select_file():
    root = Tk()
    root.geometry("1x1")  # 设置窗口大小为1x1像素，这样它只会在任务栏上显示一个图标
    root.attributes('-alpha', 0.1)  # 设置窗口透明度，使其几乎不可见

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
