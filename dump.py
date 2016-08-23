from cancom.hw import cantact

# default value (Ubuntu) for first cantact device
dev = cantact.CantactDev("/dev/ACM0")

# comfort CAN
dev.set_bitrate(100000)

# start cantact
dev.start()

while True:
    print(dev.recv())