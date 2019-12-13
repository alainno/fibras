from fiberrandom import FiberSample
from PIL import Image,ImageDraw
import math
import numpy as np

def createFiberWave():

    # trazar una línea aleatoria con u radomness

    # trazar onda senoidal
    # obtener la longitud de la recta aleatoria (time)
    # generar amplitud
    # obtener angulo de la recta aleatoria
    # rotar

    fiberSample = FiberSample(256, 256)

    # img = fiberSample.createFiberSample(1, 5, 5)
    # img.show()

    points = fiberSample.createRandomLine()

    print(points)

    img = Image.new('RGB', (fiberSample.width, fiberSample.height), "black")
    draw = ImageDraw.Draw(img)
    draw.line(points, fill=(255, 255, 255), width=1)
    #img.show()

    perp_points = fiberSample.getPerpendicular(points)

    print(perp_points)

    draw.line(perp_points, fill=(255, 255, 255), width=1)

    #img.show()

    #return img

    distance = getDistance(perp_points)
    print('distance:', round(distance))

    time = np.arange(0, distance, 1)
    amplitude = np.sin(0.01 * time)

    x1, x2 = perp_points[0]
    y1, y2 = perp_points[1]

    m = (y2-y1)/(x2-x1)
    angle = math.degrees(math.atan(m))

    xy_sine = []
    xy_points = []
    pond = 5
    mitad = fiberSample.height/2

    for i, a in enumerate(amplitude):
        xy_sine.append(time[i])
        xy_sine.append(mitad - round(a * pond))

        point = rotate((0, 0), (time[i], round(a * pond)), math.radians(angle + 90))

        xy_points.append(point[0])
        xy_points.append(mitad - point[1])

    draw.line(xy_points, fill=(255, 255, 255), width=2)

    print('angle:', angle)

    img.show()

def getDistance(line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


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

# crear una imagen con una linea ondeada desde un punto x1,y1 hasta un punto x2,y2
#img = createFiberWave(x1,y2,x2,y2)

#img.show()

if __name__ == "__main__":
    createFiberWave()