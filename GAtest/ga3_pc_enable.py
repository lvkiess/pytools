import socket
from wetest.gautomator3 import Client, By, Context

# Create socket by address or socket, including sockets created from adbutils and tidevice.
sock = socket.socket()
sock.connect(("127.0.0.1", 27029))

# Create client through socket
client = Client(addr=sock, timeout=5)
client1 = Client(addr=("127.0.0.1", 27029), timeout=5)


client1.find_element(Context.Slate, By.Text, "OPTIONS").click()
