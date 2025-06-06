import re

def extract_coordinates(log_str):
    pattern = r'X=([-+]?\d*\.\d+) Y=([-+]?\d*\.\d+) Z=([-+]?\d*\.\d+)'
    match = re.search(pattern, log_str)
    if match:
        return match.groups()
    else:
        raise ValueError("Invalid Log Input")

def format_editor(x, y, z):
    return f"(X={x},Y={y},Z={z})"

def format_moveto(x, y, z):
    return f"{int(float(x))} {int(float(y))} {int(float(z))} 0"

def format_gm(x, y, z):
    return f"gm moveto {x} {y} {z} 0"

def format_adb(x, y, z):
    return f'adb shell "am broadcast -a android.intent.action.RUN -e cmd \'{format_gm(x, y, z)}\'"'