import os
from adbutils import adb
import socket
from wetest.gautomator3 import Client, By, Context


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        print(type(s))
        port = s.getsockname()[1]
    return port


# 连接到设备
adb_client = adb.device()

# 分配一个空闲端口（如果需要动态分配）
engine_port = find_free_port()
print(engine_port)
# 将设备的端口转发到本地端口
adb_client.forward(local=f"tcp:{engine_port}", remote="tcp:27029")

# 初始化 Client
client = Client(addr=("127.0.0.1", engine_port), timeout=5)

client.find_element(Context.Slate, By.Text, "OPTIONS").click()
