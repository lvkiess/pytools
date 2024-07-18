import requests
from datetime import datetime
import sys

url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3b4b7832-4e73-4e72-aa20-5e4685b126a5"
headers = {"Content-Type": "application/json"}
current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if len(sys.argv) == 2:
    message = sys.argv[1]
else:
    message = ""

data = {
    "msgtype": "text",
    "text": {
        "content": f"打包结果: {current_timestamp} 【{message}】",
    },
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
