from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import json
from draws_logic import draw_results, matplotlib_colors, format_pie_label, draw_card

pie_canvas = None


# 执行多次十连抽，并显示饼状图
def do_multiple_ten_draws(num_times, result_frame):
    # 初始化抽卡结果统计
    card_stats = {'SSR': 0, 'SR': 0, 'R': 0, 'N': 0}
    global pie_canvas

    # 如果有旧的饼状图，先销毁它
    if pie_canvas is not None:
        pie_canvas.get_tk_widget().destroy()
        pie_canvas = None

    # 进行多次十连抽
    for _ in range(num_times):
        draw_card(10, result_frame)
        # 更新统计
        for card_type in card_stats:
            card_stats[card_type] += draw_results.count(card_type)

    json_results = json.dumps(card_stats, indent=4)  # indent=4 使得输出更易读

    # 打印JSON结果到控制台
    print(json_results)
    # 绘制饼状图
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
    ax.pie(card_stats.values(), labels=card_stats.keys(),
           colors=[matplotlib_colors[card_type] for card_type in card_stats.keys()],
           autopct=lambda pct: format_pie_label(pct, card_stats.values()), startangle=90)
    ax.axis('equal')  # 确保饼图是圆形

    # 销毁旧的画布（如果存在）并创建新的画布
    for widget in result_frame.winfo_children():
        widget.destroy()
    pie_canvas = FigureCanvasTkAgg(fig, master=result_frame)
    pie_canvas.draw()
    pie_canvas.get_tk_widget().pack(pady=20)
