from PIL import Image,ImageDraw
from random import randint

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
        #limit = self.width / 2
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

        #return self.fiberLine(dx, dy)
        #return self.perpendicular_line(dx, dy)

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


if __name__ == "__main__":
    fiberSample = FiberSample(400,300)
    #createFiberImage(size, width, testDir)

    print('Generate fiber sample with random widths')
    img = fiberSample.createFiberSample(1, 5, 5)
    #img.save("fiber-sample.png", "PNG")
    img.show()

