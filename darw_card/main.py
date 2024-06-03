import tkinter as tk
from tkinter import simpledialog, messagebox

from display_results import do_multiple_ten_draws
from draws_logic import draw_card

# 创建主窗口
root = tk.Tk()
root.title("手游抽卡模拟器")

# 创建结果框架
result_frame = tk.Frame(root)
result_frame.pack(pady=20)


def input_ten_draw_times():
    try:
        times = int(simpledialog.askstring("输入", "请输入要进行多少次十连抽："))
        if times <= 0:
            messagebox.showerror("错误", "输入的次数必须为正整数！")
            return
        do_multiple_ten_draws(times, result_frame)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数！")


# 创建抽卡按钮并绑定函数
single_draw_button = tk.Button(root, text="单抽", command=lambda: draw_card(1,result_frame))
single_draw_button.pack(pady=10)

ten_draw_button = tk.Button(root, text="十连抽", command=lambda: draw_card(10,result_frame))
ten_draw_button.pack(pady=10)

# 创建进行多次十连抽的按钮
multiple_ten_draw_button = tk.Button(root, text="多次十连抽", command=input_ten_draw_times)
multiple_ten_draw_button.pack(pady=10)

# 进入主循环
root.mainloop()
