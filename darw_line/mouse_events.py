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
        if event.button == 1 and is_dragging and press is not None:  # 检查 press 是否为 None
            dx = event.xdata - press[0]
            dy = event.ydata - press[1]
            ax.set_xlim(ax.get_xlim() - dx)
            ax.set_ylim(ax.get_ylim() - dy)

            # 使用 blit 更新背景
            fig.canvas.restore_region(background)
            ax.draw_artist(ax.patch)
            ax.draw_artist(ax.xaxis)
            ax.draw_artist(ax.yaxis)
            for artist in ax.get_children():
                if isinstance(artist, plt.Line2D):
                    ax.draw_artist(artist)
            fig.canvas.blit(ax.bbox)

            press = (event.xdata, event.ydata)

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
