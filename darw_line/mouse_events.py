import matplotlib.pyplot as plt

press = None
is_dragging = False


def connect_mouse_events(fig, ax, enable_zoom=True, enable_pan=True, background=None):
    global press, is_dragging
    background = fig.canvas.copy_from_bbox(ax.bbox)

    def on_press(event):
        global press, is_dragging
        if event.button == 1:
            press = (event.xdata, event.ydata)
            is_dragging = True  # 鼠标左键按下，开始拖动

    def on_release(event):
        global press, is_dragging
        press = None
        is_dragging = False  # 鼠标左键释放，停止拖动
        plt.gcf().canvas.draw_idle()

    def on_motion(event):
        global press, is_dragging
        if event.inaxes is None:  # 确保事件在绘图区域内
            return
        if event.button == 1 and is_dragging:  # 鼠标左键按下并拖动
            if press is None:  # 如果 press 是 None，则设置初始坐标
                press = (event.xdata, event.ydata)
            else:
                dx = event.xdata - press[0]
                dy = event.ydata - press[1]

                # 更新图形的 x 和 y 限制
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()
                ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
                ax.set_ylim(ylim[0] - dy, ylim[1] - dy)

                # 使用 blit 更新背景
                fig.canvas.restore_region(background)

                # 重绘所有的艺术家
                ax.draw_artist(ax.patch)
                ax.draw_artist(ax.xaxis)
                ax.draw_artist(ax.yaxis)
                for artist in ax.get_children():
                    if isinstance(artist, plt.Line2D):
                        ax.draw_artist(artist)

                # 更新 blit 区域
                fig.canvas.blit(ax.bbox)

    def on_scroll(event):
        factor = 0.9 if event.button == 'up' else 1.1
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        center_x, center_y = event.xdata, event.ydata
        width, height = xlim[1] - xlim[0], ylim[1] - ylim[0]
        new_width, new_height = width * factor, height * factor
        new_xlim = (center_x - new_width / 2, center_x + new_width / 2)
        new_ylim = (center_y - new_height / 2, center_y + new_height / 2)
        ax.set_xlim(new_xlim)
        ax.set_ylim(new_ylim)
        plt.gcf().canvas.draw_idle()

    if enable_zoom:
        fig.canvas.mpl_connect('scroll_event', on_scroll)
    if enable_pan:
        fig.canvas.mpl_connect('button_press_event', on_press)
        fig.canvas.mpl_connect('button_release_event', on_release)
        fig.canvas.mpl_connect('motion_notify_event', on_motion)

    return fig, ax
