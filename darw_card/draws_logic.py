import random
from tkinter import ttk
import matplotlib.colors as mcolors

# 定义卡牌类型及其出现的概率
card_probs = {
    'SSR': 0.05,
    'SR': 0.3,
    'R': 0.5,
    'N': 0.15
}
card_types = list(card_probs.keys())

# 定义卡牌类型及其对应的颜色
card_colors = {
    'SSR': 'gold',
    'SR': 'purple',
    'R': 'blue',
    'N': 'green'
}
matplotlib_colors = {k: mcolors.to_rgba(v) for k, v in card_colors.items()}


def format_pie_label(pct, allvals):
    absolute = int(round(pct / 100. * sum(allvals)))
    return "{:.1f}% ({}draws)".format(pct, absolute)


# 根据概率分布生成一张随机卡牌
def draw_random_card():
    total_prob = sum(card_probs.values())
    rand_num = random.uniform(0, total_prob)
    cumulative_prob = 0
    for card_type, prob in card_probs.items():
        cumulative_prob += prob
        if rand_num < cumulative_prob:
            return card_type


# 初始化抽卡结果列表
draw_results = []


# 抽卡函数
def draw_card(times, result_frame):
    global draw_results
    draw_results.clear()
    for _ in range(times):
        card_type = draw_random_card()
        draw_results.append(card_type)
    update_result_label(result_frame)


# 更新结果标签的函数
def update_result_label(result_frame):
    # 清除之前的标签
    for widget in result_frame.winfo_children():
        widget.destroy()

    # 竖行显示抽卡结果，并设置颜色
    for i, card_type in enumerate(draw_results):
        color = card_colors[card_type]
        result_label = ttk.Label(result_frame, text=card_type, foreground=color)
        result_label.grid(row=i, column=0, pady=5)
