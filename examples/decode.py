from cancom import can, bus
from cancom.file import jsondb
from cancom.hw import socketcan

parser = jsondb.JsonDbParser()
b = parser.parse('example_db.json')

dev = socketcan.SocketCanDev('vcan0')
dev.start()

while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            print(s)
