from cancom import can
from cancom.hw import cantact
import time

# default value (Ubuntu) for first cantact device
dev = cantact.CantactDev("/dev/ttyACM0")

# comfort CAN
dev.set_bitrate(100000)

# start cantact
dev.start()

DRIVER_UP = can.Frame(0x182, 3, [0x20, 0x00, 0x00])

for x in range(0, 10000):
    dev.send(DRIVER_UP)
    time.sleep(.25)