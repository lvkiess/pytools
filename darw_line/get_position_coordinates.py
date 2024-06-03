import re
import tkinter as tk
from tkinter import messagebox


def parse_input(input_str):
    pattern = r'\(X=([-\d.]+),Y=([-\d.]+),Z=([-\d.]+)\)'
    matches = re.findall(pattern, input_str)
    points = []
    for match in matches:
        point = {"X": float(match[0]), "Y": float(match[1]), "Z": float(match[2])}
        points.append(point)
    return points
