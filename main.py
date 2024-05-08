from tkinter.messagebox import showinfo
from file_selection import select_file
from excel_processing import process_excel


def main():
    input_files = select_file()

    if input_files:
        process_excel(input_files)
    else:
        showinfo("取消", "未选择文件，操作已取消。")


if __name__ == "__main__":
    main()
