from PIL import Image,ImageDraw
from random import randint

class FiberSample():

    def __init__(self, width=256, height=256):
        self.width = width
        self.height = height
        #print("Width: ", str(self.witdh))

    def fiberLine(self, dx, dy):
        centro = self.width / 2, self.height / 2

        x, y = centro[0] + dx, centro[1] + dy
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
            if(i%4==0):
                lines.append(self.fiberLine(-self.randValue(xlimit), -self.randValue(ylimit)))
            elif(i%4==1):
                lines.append(self.fiberLine(-self.randValue(xlimit), self.randValue(ylimit)))
            elif(i%4==2):
                lines.append(self.fiberLine(self.randValue(xlimit), -self.randValue(ylimit)))
            elif(i%4==3):
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


fiberSample = FiberSample(100,300)
#createFiberImage(size, width, testDir)

print('Generate fiber sample with random widths')
img = fiberSample.createFiberSample(20, 1, 20)
img.save("fiber-sample.png", "PNG")

