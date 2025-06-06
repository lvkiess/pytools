import re


def process_log_file(file_path):
    try:
        with open(file_path, "r") as file:
            log_lines = file.readlines()

        # 查找满足条件的日志行
        result_lines = []
        pattern = r"LogBlueprintUserMessages: \[VRising_WP\] X=\d+\.\d+ Y=\d+\.\d+ Z=-\d+\.\d+"
        for line in log_lines:
            if re.search(pattern, line):
                result_lines.append(line.strip())

        return result_lines
    except Exception as e:
        return [f"Error: {str(e)}"]