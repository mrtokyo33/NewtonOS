from .mru import *

v = Velocity(3)
m = Motion(v, (1, 0, 0))

print(m.getTimeToReachPosition((0, 0, 0)))
print(m.getTimeToReachPosition((1, 0, 1)))