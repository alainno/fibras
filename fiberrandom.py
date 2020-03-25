from PIL import Image,ImageDraw
from random import randint
import math
import numpy as np

from rand_images import emptyDir

class FiberSample():

    def __init__(self, width=256, height=256):
        self.width = width
        self.height = height
        #print("Width: ", str(self.witdh))

    def perpendicular_y(self,m,x1,y1,x):
        return (y1 - (x - x1)/m)

    def perpendicular_x(self,m,x1,y1,y):
        return (x1 - (y - y1)*m)

    def perpendicular_line(self, dx, dy):
        points = []
        m = dy / dx
        cx, cy = self.width / 2, self.height / 2
        x1, y1 = cx + dx, cy + dy

        print('x1:', x1, 'y1:', y1)

        x = 0
        y = self.perpendicular_y(m, x1, y1, x)

        if(y < 0 or y > self.height):
            x = self.perpendicular_x(m, x1, y1, y)
            if(y<0):
                y=0
            elif(y>self.height):
                y=self.height

        points.append((round(x),round(y)))

        x = self.width
        y = self.perpendicular_y(m, x1, y1, x)

        if (y < 0 or y > self.height):
            x = self.perpendicular_x(m, x1, y1, y)
            if (y < 0):
                y = 0
            elif (y > self.height):
                y = self.height

        points.append((round(x), round(y)))
        return points


    def fiberLine(self, dx, dy):
        #centro = self.width / 2, self.height / 2
        cx, cy = self.width / 2, self.height / 2

        #x, y = centro[0] + dx, centro[1] + dy
        x, y = cx + dx, cy + dy
        m = dy / dx

        if (dx < 0):
            ox = 0
        else:
            ox = self.width

        if (dy < 0):
            oy = 0
        else:
            oy = self.height

        y_ = y - (ox - x) / m
        x_ = x - (oy - y) * m

        return [(ox, y_), (x_, oy)]

    def randValue(self,limit):
        return randint(1, limit)

    def createRandomLines(self, total):
        lines = []
        xlimit = self.width / 2
        ylimit = self.height / 2

        for i in range(total):
            mod = i%4
            if(mod==0):
                lines.append(self.fiberLine(-self.randValue(xlimit), -self.randValue(ylimit)))
            elif(mod==1):
                lines.append(self.fiberLine(-self.randValue(xlimit), self.randValue(ylimit)))
            elif(mod==2):
                lines.append(self.fiberLine(self.randValue(xlimit), -self.randValue(ylimit)))
            elif(mod==3):
                lines.append(self.fiberLine(self.randValue(xlimit), self.randValue(ylimit)))

        return lines

    def drawFibers(self, img, lines, min_width, max_width):
        draw = ImageDraw.Draw(img)
        for line in lines:
            draw.line(line, fill=(255, 255, 255), width=randint(min_width,max_width))

    def createFiberSample(self, fiber_number, min_width, max_width):
        img = Image.new('RGB', (self.width, self.height), "black")
        lines = self.createRandomLines(fiber_number)
        self.drawFibers(img, lines, min_width, max_width)
        return img

    def createRandomLine(self):
        xlimit = self.width / 2
        ylimit = self.height / 2
        cuadrante_a = 1 - randint(0, 1)*2
        cuadrante_b = 1 - randint(0, 1)*2
        #print('cuadrante a:',cuadrante_a)
        #print('cuadrante b:',cuadrante_b)

        dx = self.randValue(xlimit)*cuadrante_a
        dy = self.randValue(ylimit)*cuadrante_b

        print('dx:', dx, 'dy:', dy)

        return [(xlimit, ylimit), (dx+xlimit, dy+ylimit)]


    def getPerpendicular(self, line):
        points = []

        cx, cy = line[0]
        x1, y1 = line[1]

        m = (y1-cy) / (x1-cx)

        print('m:', m)

        print('x1:', x1)
        print('y1:', y1)

        x = 0
        y = self.perpendicular_y(m, x1, y1, x)

        if (y < 0):
            y = 0
            x = self.perpendicular_x(m, x1, y1, y)
        elif (y > self.height):
            y = self.height
            x = self.perpendicular_x(m, x1, y1, y)

        points.append((round(x), round(y)))

        x = self.width
        y = self.perpendicular_y(m, x1, y1, x)

        if (y < 0):
            y = 0
            x = self.perpendicular_x(m, x1, y1, y)
        elif (y > self.height):
            y = self.height
            x = self.perpendicular_x(m, x1, y1, y)

        points.append((round(x), round(y)))
        return points

    def createFiberWavedSample(self, fiber_number, min_width, max_width):
        img = Image.new('RGB', (self.width, self.height), "black")
        waves = self.createRandomWaves(fiber_number)
        self.drawWavedFibers(img, waves, min_width, max_width)
        return img

    def drawWavedFibers(self, img, waves, min_width, max_width):
        draw = ImageDraw.Draw(img)
        for wave_points in waves:
            draw.line(wave_points, fill=(255, 255, 255), width=randint(min_width, max_width))

    def createRandomWaves(self, total):
        waves = []

        #waves.append([1, 1, 20, 20, 30, 30, 40, 40])
        #waves.append([50, 1, 70, 20, 80, 30, 90, 40])

        for i in range(total):
            waves.append(self.createFiberWave())
        return waves

    def createFiberWave(self):

        #fiberSample = FiberSample(256, 256)
        # trazar una línea aleatoria con u radomness
        points = self.createRandomLine()
        #print('Recta aleatoria:', points)

        perp_points = self.getPerpendicular(points)
        #print('Recta perpendicular:', perp_points)

        # trazar onda senoidal
        # obtener la longitud de la recta aleatoria (time)
        distance = self.getDistance(perp_points)
        print('distance:', round(distance))
        time = np.arange(0, distance, 1)
        # print('time:', time)

        # generar amplitud
        amplitude = np.sin(0.05 * time)
        # print('amplitud:', amplitude)

        # obtener angulo de la recta aleatoria
        x1, y1 = perp_points[0]
        x2, y2 = perp_points[1]
        m = (y2 - y1) / (x2 - x1)
        angle = math.atan(m)
        print('angle:', math.degrees(angle))

        # rotar

        sine_points = []
        rotated_points = []
        pond = 5
        #mitad = fiberSample.height / 2

        for i, a in enumerate(amplitude):
            sine_points.append(time[i] + x1)
            sine_points.append(y1 - round(a * pond))

            point = self.rotate((0, 0), (time[i], round(a * pond)), -angle)

            rotated_points.append(point[0] + x1)
            rotated_points.append(y1 - point[1])

        return rotated_points

    # obtiene la distancia euclideana entre dos puntos
    def getDistance(self, line):
        x1, y1 = line[0]
        x2, y2 = line[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def rotate(self, origin, point, angle):
        """
        Rotate a point counterclockwise by a given angle around a given origin.
        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return qx, qy

    def getWavePoints(self):
        pass


if __name__ == "__main__":
    fiberSample = FiberSample(256,256)
    #createFiberImage(size, width, testDir)

    print('Generate fiber sample with random widths')
    #img = fiberSample.createFiberSample(10, 1, 5)
    #img = fiberSample.createFiberWavedSample(15, 12, 12)
    #img.save("fiber-sample.png", "PNG")
    #img.show()

    testDir = "data/test"
    emptyDir(testDir)

    for i in range(20):
        img = fiberSample.createFiberWavedSample(16, i+1, i+1)
        img.save(testDir + "/" + str(i + 1).zfill(4) + ".png", "PNG")


