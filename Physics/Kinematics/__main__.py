from .mru import *

v = Velocity(10, 45, 45)
m = Motion(v, (1, 0, -1))
print(m.getPositionAfterXSeconds(3))