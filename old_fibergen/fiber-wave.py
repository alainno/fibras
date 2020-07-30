from fiberrandom import FiberSample
from PIL import Image,ImageDraw
import math
import numpy as np

def createFiberWave():

    fiberSample = FiberSample(256, 256)
    # trazar una línea aleatoria con u radomness
    points = fiberSample.createRandomLine()
    print('Recta aleatoria:', points)

    perp_points = fiberSample.getPerpendicular(points)
    print('Recta perpendicular:', perp_points)

    # trazar onda senoidal
    # obtener la longitud de la recta aleatoria (time)
    distance = getDistance(perp_points)
    print('distance:', round(distance))
    time = np.arange(0, distance, 1)
    #print('time:', time)

    # generar amplitud
    amplitude = np.sin(0.01 * time)
    #print('amplitud:', amplitude)

    # obtener angulo de la recta aleatoria
    x1, y1 = perp_points[0]
    x2, y2 = perp_points[1]
    m = (y2-y1)/(x2-x1)
    angle = math.atan(m)
    print('angle:', math.degrees(angle))

    # rotar

    sine_points = []
    rotated_points = []
    pond = 5
    mitad = fiberSample.height/2

    for i, a in enumerate(amplitude):
        sine_points.append(time[i] + x1)
        sine_points.append(y1 - round(a * pond))

        point = rotate((0, 0), (time[i], round(a * pond)), -angle)

        rotated_points.append(point[0] + x1)
        rotated_points.append(y1 - point[1])

    # Mostrando proceso a tráves de rectas
    img = Image.new('RGB', (fiberSample.width, fiberSample.height), "black")
    draw = ImageDraw.Draw(img)
    draw.line(points, fill=(255, 255, 255), width=1)
    draw.line(perp_points, fill=(255, 0, 0), width=1)
    #draw.line(sine_points, fill=(0, 255, 0), width=1)
    draw.line(rotated_points, fill=(0, 255, 255), width=2)

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