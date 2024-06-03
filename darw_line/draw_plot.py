import matplotlib.pyplot as plt


def draw_point_link(points, show_coords=False, new_point=None):
    x_coords = [point["X"] for point in points]
    y_coords = [point["Y"] for point in points]

    fig, ax = plt.subplots(figsize=(10, 8))

    if new_point is not None:
        ax.scatter(new_point[0], new_point[1], marker="o", color="yellow", s=300)

    ax.scatter(x_coords[0], y_coords[0], marker="o", color="red", s=200)
    ax.scatter(x_coords[1:], y_coords[1:], marker="o", color="blue", s=100)

    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        ax.annotate(f"{i + 1}. {f'({x:.2f}, {y:.2f})' if show_coords else ''}", (x, y), textcoords="offset points",
                    xytext=(5, 5), ha="left", fontsize=9)

    for i in range(len(x_coords) - 1):
        x_mid = (x_coords[i] + x_coords[i + 1]) / 2
        y_mid = (y_coords[i] + y_coords[i + 1]) / 2
        dx = x_coords[i + 1] - x_coords[i]
        dy = y_coords[i + 1] - y_coords[i]
        ax.arrow(x_mid - dx / 4, y_mid - dy / 4, dx / 2, dy / 2,
                 head_width=400, head_length=400, head_starts_at_zero=False, length_includes_head=True, fc="k",
                 linewidth=1)
        ax.plot([x_coords[i], x_coords[i + 1]], [y_coords[i], y_coords[i + 1]], color="k", linewidth=1)

    ax.set_xlabel("X-axis", fontsize=14)
    ax.set_ylabel("Y-axis", fontsize=14)
    ax.set_title("XY Plane Plot", fontsize=16)
    ax.grid(True)
    ax.invert_yaxis()
    plt.tight_layout()

    return fig, ax
