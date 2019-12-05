import math
import matplotlib.pyplot as plt

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


point = (3,4)
origin = (0,0)

rotated = rotate(origin, point, math.radians(5))
#print(rotated)
plt.scatter(origin[0],origin[1])
plt.scatter(point[0],point[1])
plt.scatter(rotated[0],rotated[1])
plt.show()



