#import argparse

import sys
from skimage import img_as_bool, io, color, morphology
from utils import pruning, getSkeletonIntersection, removeCross
import matplotlib.pyplot as plt

#print("hola mundo")

#parser = argparse.ArgumentParser(description='Demo.')
#args = parser.parse_args()
#type(args)
#print(args[0])

imgPath = sys.argv[1]
#print(sys.argv[1])
try:
    image = img_as_bool(color.rgb2gray(io.imread(imgPath)))
    print('Image Matrix:')
    print(image)
except ValueError as e:
    print(e)

skeleton, distance = morphology.medial_axis(image, mask=None, return_distance=True)
#print(distance)
thinned = morphology.thin(image)
prunned2 = pruning(thinned,3)
intersecciones = getSkeletonIntersection(prunned2)

print(intersecciones)

uncrossed = prunned2.copy()

for cross in intersecciones:
  uncrossed = removeCross(cross, distance, uncrossed)

rows, cols = uncrossed.shape

diameters = dict()

for x in range(0, rows):
    for y in range(0, cols):
        # print(uncrossed[x][y])
        if (uncrossed[x, y]):
            # obtener ancho
            # print(distanceMap[x,y].astype('uint8')*2)
            diameter = distance[x, y].astype('uint8') * 2

            if (diameter in diameters):
                diameters[diameter] += 1
            else:
                diameters[diameter] = 1
            # else:
            #  diameters[diameter] += 1
            # print(diameter)

print(diameters)

plt.bar(list(diameters.keys()), diameters.values())
plt.ylabel('Frecuencia')
plt.xlabel('Diámetros')
plt.savefig('histogram.png')
