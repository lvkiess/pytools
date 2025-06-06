import tkinter as tk
from tkinter import ttk, filedialog, Text
from coordinate import extract_coordinates, format_editor, format_moveto, format_gm, format_adb
from findlog import process_log_file  # 导入日志处理逻辑

# 原有功能的实现代码保持不变
def convert_from_log_to_editor_moveto_gm_adb():
    try:
        x, y, z = extract_coordinates(entry_log.get().strip())
        entry_editor.delete(0, tk.END)
        entry_editor.insert(0, format_editor(x, y, z))
        entry_moveto.delete(0, tk.END)
        entry_moveto.insert(0, format_moveto(x, y, z))
        entry_gm.delete(0, tk.END)
        entry_gm.insert(0, format_gm(x, y, z))
        entry_adb.delete(0, tk.END)
        entry_adb.insert(0, format_adb(x, y, z))
    except ValueError as e:
        display_error(e)

def convert_from_editor_to_moveto_gm_adb():
    try:
        coord_str = entry_editor.get().strip()
        stripped_str = coord_str.strip('() ')
        parts = stripped_str.split(',')
        x, y, z = next(part.split('=')[1] for part in parts if part.startswith('X')), \
                  next(part.split('=')[1] for part in parts if part.startswith('Y')), \
                  next(part.split('=')[1] for part in parts if part.startswith('Z'))
        entry_moveto.delete(0, tk.END)
        entry_moveto.insert(0, format_moveto(x, y, z))
        entry_gm.delete(0, tk.END)
        entry_gm.insert(0, format_gm(x, y, z))
        entry_adb.delete(0, tk.END)
        entry_adb.insert(0, format_adb(x, y, z))
    except Exception as e:
        display_error("Invalid Editor Input")

def convert_from_moveto_to_editor_gm_adb():
    try:
        moveto_str = entry_moveto.get().strip().split()
        if len(moveto_str) == 4:
            x, y, z = moveto_str[0], moveto_str[1], moveto_str[2]
            entry_editor.delete(0, tk.END)
            entry_editor.insert(0, format_editor(x, y, z))
            entry_gm.delete(0, tk.END)
            entry_gm.insert(0, format_gm(x, y, z))
            entry_adb.delete(0, tk.END)
            entry_adb.insert(0, format_adb(x, y, z))
        else:
            display_error("Invalid Moveto Input")
    except Exception as e:
        display_error("Invalid Moveto Input")

def display_error(message):
    entry_editor.delete(0, tk.END)
    entry_moveto.delete(0, tk.END)
    entry_gm.delete(0, tk.END)
    entry_adb.delete(0, tk.END)
    entry_editor.insert(0, message)
    entry_moveto.insert(0, message)
    entry_gm.insert(0, message)
    entry_adb.insert(0, message)

# 新增功能：处理日志文件并显示结果
def process_and_display_log():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log"), ("All files", "*.*")])  # 修改为支持 .log 文件
    if not file_path:
        return  # 如果用户取消选择文件，直接返回

    result_lines = process_log_file(file_path)  # 调用日志处理逻辑
    text_display.delete(1.0, tk.END)  # 清空文本显示区域
    for line in result_lines:
        text_display.insert(tk.END, line + "\n")

# 创建主窗口
root = tk.Tk()
root.title("Coordinate Converter")

# 创建并布局输入框和标签
label_log = ttk.Label(root, text="Log:")
label_log.grid(row=0, column=0, padx=10, pady=10)
entry_log = ttk.Entry(root, width=50)
entry_log.insert(0, "[2024.12.23-14.43.29:404][794]LogBlueprintUserMessages: [VRising_WP] X=41157.811 Y=109165.227 Z=-1106.595")
entry_log.grid(row=0, column=1, padx=10, pady=10)
button_log_to_editor_moveto_gm_adb = ttk.Button(root, text="Convert Log to Editor, Moveto, GM, and ADB", command=convert_from_log_to_editor_moveto_gm_adb)
button_log_to_editor_moveto_gm_adb.grid(row=0, column=2, padx=10, pady=10)

label_editor = ttk.Label(root, text="Editor:")
label_editor.grid(row=1, column=0, padx=10, pady=10)
entry_editor = ttk.Entry(root, width=50)
entry_editor.insert(0, "(X=-15846.780878,Y=90275.081525,Z=-760.019137)")
entry_editor.grid(row=1, column=1, padx=10, pady=10)
button_editor_to_moveto_gm_adb = ttk.Button(root, text="Convert Editor to Moveto, GM, and ADB", command=convert_from_editor_to_moveto_gm_adb)
button_editor_to_moveto_gm_adb.grid(row=1, column=2, padx=10, pady=10)

label_moveto = ttk.Label(root, text="Moveto:")
label_moveto.grid(row=2, column=0, padx=10, pady=10)
entry_moveto = ttk.Entry(root, width=50)
entry_moveto.insert(0, "-41340 92320 -640 0")
entry_moveto.grid(row=2, column=1, padx=10, pady=10)
button_moveto_to_editor_gm_adb = ttk.Button(root, text="Convert Moveto to Editor, GM, and ADB", command=convert_from_moveto_to_editor_gm_adb)
button_moveto_to_editor_gm_adb.grid(row=2, column=2, padx=10, pady=10)

label_gm = ttk.Label(root, text="GM:")
label_gm.grid(row=3, column=0, padx=10, pady=10)
entry_gm = ttk.Entry(root, width=50)
entry_gm.grid(row=3, column=1, padx=10, pady=10)

label_adb = ttk.Label(root, text="ADB:")
label_adb.grid(row=4, column=0, padx=10, pady=10)
entry_adb = ttk.Entry(root, width=50)
entry_adb.grid(row=4, column=1, padx=10, pady=10)

# 新增功能的布局
button_open_file = ttk.Button(root, text="Open Log File", command=process_and_display_log)
button_open_file.grid(row=5, column=0, padx=10, pady=10)

text_display = Text(root, height=10, width=50)  # 创建文本显示区域
text_display.grid(row=5, column=1, padx=10, pady=10)

# 进入主事件循环
root.mainloop()
