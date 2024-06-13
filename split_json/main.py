import json
import tkinter as tk


def split_case(json_str):
    json_data = json.loads(json_str)
    actions = json_data["Actions"]
    result = []
    for action in actions:
        sub_json_data = {"Actions": [action]}
        result.append(json.dumps(sub_json_data, indent=2))
    return result


def get_action_description(action_list):
    action_description_map = {
        "DriveTo": "自动驾驶",
        "AutoFight": "自动战斗",
        "MoveTo": "自动移动"
    }
    for action in action_list:
        if isinstance(action, list):
            for sub_action in action:
                if isinstance(sub_action, dict) and sub_action["method"] in action_description_map:
                    return action_description_map[sub_action["method"]]
        elif isinstance(action, dict):
            if action["method"] in action_description_map:
                return action_description_map[action["method"]]
    return ""


def on_split_button_click():
    json_str = input_text.get("1.0", "end-1c")
    split_json_list = split_case(json_str)

    for child in output_frame.winfo_children():
        child.destroy()

    columns = 1
    if len(split_json_list) > 5:
        columns = 2
    if len(split_json_list) > 8:
        columns = 3

    row = 0
    column = 0
    for index, split_json in enumerate(split_json_list):
        action_str = json.loads(split_json)["Actions"][0]
        action_description = get_action_description(action_str)
        label = tk.Label(output_frame, text=f"子 Action {index + 1} {action_description}:")
        label.grid(row=row, column=column, sticky="w")

        output_text = tk.Text(output_frame, wrap="word", width=50, height=10)
        output_text.insert("1.0", split_json)
        output_text.config(state="disabled")
        output_text.grid(row=row + 1, column=column, sticky="w", padx=10, pady=10)

        column += 1
        if column == columns:
            row += 2
            column = 0


root = tk.Tk()
root.title("拆分 Action")

input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill="both", expand=True)

input_label = tk.Label(input_frame, text="输入 Action:")
input_label.pack(anchor="w")

input_text = tk.Text(input_frame, wrap="word", width=50, height=10)
input_text.pack(anchor="w", padx=10, pady=10, fill="both", expand=True)

button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

split_button = tk.Button(button_frame, text="拆分 Action", command=on_split_button_click)
split_button.pack()

output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
