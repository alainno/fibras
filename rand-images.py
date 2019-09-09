from tqdm import tqdm
from PIL import Image,ImageDraw
from random import randint

def drawRandomFiber(img, lines, width):
    d = ImageDraw.Draw(img)
    #d.line([(0,0),(50,50)], fill=(255, 255, 255), width=1)
    for line in lines:
        d.line(line, fill=(255, 255, 255), width=width)

def fiberLine(size, dx, dy):
    centro = size / 2, size / 2

    x, y = centro[0] + dx, centro[1] + dy
    m = dy / dx

    # print('m =',m)

    if (dx < 0):
        ox = 0
    else:
        ox = size
    if (dy < 0):
        oy = 0
    else:
        oy = size

    # y_ - y = -(1/m)*(x_ - x)
    y_ = y - (ox - x) / m
    x_ = x - (oy - y) * m

    # print('x_,y_ =',x_,y_)

    return [(ox, y_), (x_, oy)]

def randValue(limit):
  return randint(1,limit)

def randomLines(size):
    lines = []
    limit = size / 2

    for i in range(4):
        lines.append(fiberLine(size, -randValue(limit), -randValue(limit)))
        lines.append(fiberLine(size, -randValue(limit), randValue(limit)))
        lines.append(fiberLine(size, randValue(limit), -randValue(limit)))
        lines.append(fiberLine(size, randValue(limit), randValue(limit)))

    return lines

def createFiberImage(size, width, directory):
    img = Image.new('RGB', (size, size), "black")
    randLines = randomLines(size)
    drawRandomFiber(img, randLines, width)
    img.save(directory + "/" + str(i + 1).zfill(4) + ".png", "PNG")

import os, shutil

def emptyDir(folder):
    #folder = '/path/to/folder'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


thickTrainDir = "data/train/thick"
thinTrainDir = "data/train/thin"
thickValDir = "data/validation/thick"
thinValDir = "data/validation/thin"
size = 300
totalTrain = 100
totalVal = 20
thickWidth = 12
thinWidth = 4

emptyDir(thickTrainDir)
emptyDir(thinTrainDir)
emptyDir(thickValDir)
emptyDir(thinValDir)

# train
for i in tqdm(range(totalTrain)):
    createFiberImage(size, thickWidth, thickTrainDir)
    createFiberImage(size, thinWidth, thinTrainDir)

# val
for i in tqdm(range(totalVal)):
    createFiberImage(size, thickWidth, thickValDir)
    createFiberImage(size, thinWidth, thinValDir)


