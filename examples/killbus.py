from cancom import can
from cancom.hw import peak
from cancom.hw import socketcan

#dev = peak.PcanDev()
dev = socketcan.SocketCanDev("vcan0")

dev.start()

frame = can.Frame(0)
frame.dlc = 8

while True:
    dev.send(frame)
