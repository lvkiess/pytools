from tkinter import Tk, Button, Label

from file_selection import select_directory, select_multiple_files


def main():
    root = Tk()
    root.title("测试结果统计")

    # 创建并放置按钮
    Label(root, text="请选择操作方式:").pack(pady=10)
    Button(root, text="打开目录中的所有表格", command=select_directory).pack(pady=5)
    Button(root, text="打开多个表格", command=select_multiple_files).pack(pady=5)

    # 运行Tkinter事件循环
    root.mainloop()


if __name__ == "__main__":
    main()
