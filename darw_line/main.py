import tkinter as tk
from tkinter import messagebox, simpledialog
from get_position_coordinates import parse_input
from draw_plot import draw_point_link
from mouse_events import connect_mouse_events
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def on_convert():
    input_str = input_box.get("1.0", "end-1c")
    try:
        global points
        points = parse_input(input_str)
        output_box.delete("1.0", "end")
        output_str = "\n".join([str(point) for point in points])
        output_box.insert("1.0", output_str)
    except ValueError as e:
        messagebox.showerror("错误", str(e))


def on_plot(new_point=None):
    global canvas
    if points is None:
        messagebox.showerror("错误", "请先转换输入数据。")
        return

    show_coords_value = show_coords_var.get()
    fig, ax = draw_point_link(points, show_coords=show_coords_value, new_point=new_point)
    fig, ax = connect_mouse_events(fig, ax, enable_zoom=True, enable_pan=True)
    if canvas is not None:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


def add_point():
    try:
        x, y = map(float, simpledialog.askstring("添加点", "请输入 X 和 Y 坐标，用逗号分隔：").split(','))
        on_plot(new_point=(x, y))
    except ValueError as e:
        messagebox.showerror("错误", "输入的坐标格式不正确。")
        print(e)


root = tk.Tk()
root.title("点转换与绘图")

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

input_label = tk.Label(left_frame, text="输入数据:")
input_label.pack()

input_box = tk.Text(left_frame, wrap="word", width=30, height=10)
input_box.pack()

convert_button = tk.Button(left_frame, text="转换数据", command=on_convert)
convert_button.pack()

output_label = tk.Label(left_frame, text="转换后的数据:")
output_label.pack()

output_box = tk.Text(left_frame, wrap="word", width=30, height=10)
output_box.pack()

show_coords_var = tk.BooleanVar()
show_coords_check = tk.Checkbutton(left_frame, text="在点边上显示坐标", variable=show_coords_var)
show_coords_check.pack()

plot_button = tk.Button(left_frame, text="绘制点", command=lambda: on_plot())
plot_button.pack()

add_point_button = tk.Button(left_frame, text="添加点", command=add_point)  # 新增按钮
add_point_button.pack()

plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

points = None
canvas = None

root.mainloop()
