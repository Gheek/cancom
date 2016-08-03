from cancom import can
from cancom.hw import socketcan

dev = socketcan.SocketCanDev("vcan0")

dev.start()
while True:
    print(dev.recv())