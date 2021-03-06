from cancom.proto.obdii import ObdInterface

from cancom.hw.cantact import CantactDev
from cancom.hw.loopback import LoopbackDev
import sys

#d = LoopbackDev()
d = CantactDev(sys.argv[1])
d.set_bitrate(500000)

p = ObdInterface(d)

# read engine RPM
# mode 1, PID 0x0C
print(p.obd_request(0x7E8, 1, 0x0C))

