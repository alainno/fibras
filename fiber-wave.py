from fiberrandom import FiberSample
from PIL import Image,ImageDraw

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

    img.show()

    #return img

# crear una imagen con una linea ondeada desde un punto x1,y1 hasta un punto x2,y2
#img = createFiberWave(x1,y2,x2,y2)

#img.show()

if __name__ == "__main__":
    createFiberWave()