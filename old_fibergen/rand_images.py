from tqdm import tqdm
from PIL import Image,ImageDraw
from random import randint
import os, shutil
#from fiberrandom import FiberSample

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
    if not os.path.exists(directory):
        os.makedirs(directory)
    #emptyDir(directory)
    img = Image.new('RGB', (size, size), "black")
    randLines = randomLines(size)
    drawRandomFiber(img, randLines, width)
    img.save(directory + "/" + str(i + 1).zfill(4) + ".png", "PNG")

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

if __name__ == "__main__":
    thickTrainDir = "data/train/thick"
    thinTrainDir = "data/train/thin"
    mediumTrainDir = "data/train/medium"
    
    thickValDir = "data/validation/thick"
    thinValDir = "data/validation/thin"
    mediumValDir = "data/validation/medium"
    
    size = 256
    totalTrain = 1000
    totalVal = 200
    
    thickWidth = 12
    thinWidth = 4
    mediumWidth = 8

    emptyDir(thickTrainDir)
    emptyDir(thinTrainDir)
    emptyDir(mediumTrainDir)
    emptyDir(thickValDir)
    emptyDir(thinValDir)
    emptyDir(mediumValDir)

    # train
    print("Generating trainning images...")
    for i in tqdm(range(totalTrain)):
        createFiberImage(size, thickWidth, thickTrainDir)
        createFiberImage(size, thinWidth, thinTrainDir)
        createFiberImage(size, mediumWidth, mediumTrainDir)

    # val
    print("Generating validation images...")
    for i in tqdm(range(totalVal)):
        createFiberImage(size, thickWidth, thickValDir)
        createFiberImage(size, thinWidth, thinValDir)
        createFiberImage(size, mediumWidth, mediumValDir)

    # test
    #testDir = "data/test"
    #emptyDir(testDir)

    #print('Creando imágenes de test...')
    #for i in tqdm(range(20)):
        #createFiberImage(size, i+1, testDir)




