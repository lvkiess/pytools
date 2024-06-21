import datetime
import os
import subprocess
import time


# 检查是否连接了Android设备
def is_android_device_connected():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    for line in lines:
        if len(line) > 0 and ("device" in line or "offline" in line):
            return True
    return False


# 执行给定的adb命令
def execute_adb_command(command):
    os.system(command)


# 打开指定的本地程序
def open_local_program(path):
    os.startfile(path)


def start_app(package_name):
    try:
        subprocess.check_call(["adb", "shell", "am", "start", "-n", package_name + "/com.epicgames.unreal.SplashActivity"])
        print(f"Started app: {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start app: {e}")


# 检查指定路径下是否存在新的.utrace文件
def check_utrace_file(path):
    try:
        # 等待一段时间以确保文件生成
        time.sleep(5)

        # 获取当前时间戳
        current_timestamp = datetime.datetime.now()

        # 遍历指定路径下的所有.utrace文件
        for file in os.listdir(path):
            if file.endswith(".utrace"):
                file_path = os.path.join(path, file)

                # 获取文件的修改时间
                modified_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

                # 如果文件的修改时间晚于当前时间戳减去5秒，则认为文件是新生成的
                if modified_timestamp >= current_timestamp - datetime.timedelta(seconds=5):
                    return True

        return False
    except FileNotFoundError:
        return False


if __name__ == "__main__":
    if is_android_device_connected():
        # 执行两条指令
        execute_adb_command("adb reverse tcp:1980 tcp:1980")
        execute_adb_command("adb shell setprop debug.ue.commandline -tracehost=127.0.0.1")

        # 打开本地的UnrealInsights程序
        local_program_path = "H:\\UE_5.4\\Engine\\Binaries\\Win64\\UnrealInsights.exe"
        open_local_program(local_program_path)

        # 打开Android设备上的名为“TRing”的app
        app_package_name = "com.Tencent.TRing"
        start_app(app_package_name)

        # 检查本地路径下是否生成了新的.utrace文件
        utrace_folder_path = "C:\\Users\\chongyechen\\AppData\\Local\\UnrealEngine\\Common\\UnrealTrace\\Store\\001"
        if check_utrace_file(utrace_folder_path):
            print("新的.utrace文件已生成。")
        else:
            print("未找到新的.utrace文件。")
    else:
        print("未检测到连接的Android设备。")
