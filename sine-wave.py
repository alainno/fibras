
import numpy as np

import matplotlib.pyplot as plot

# Get x values of the sine wave

w, h = 500, 500

time = np.arange(0, w, 1)

print("time:")
print(time)

# Amplitude of the sine wave is sine of a variable like time

amplitude = np.sin(0.1*time)
print("amplitude:")
print(amplitude)


# Plot a sine wave using time and amplitude obtained for the sine wave

plot.plot(time, amplitude)

# Give a title for the sine wave plot

plot.title('Sine wave')

# Give x axis label for the sine wave plot

plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()

# Display the sine wave

plot.show()


# importing image object from PIL

#import math
from PIL import Image, ImageDraw
import aggdraw


#shape = [(10, 10), (w - 10, h - 10)]

# creating new Image object
img = Image.new("RGB", (w, h))

# create rectangle image
#img1 = ImageDraw.Draw(img)
#img1.arc(shape, start = 30, end = 1, fill ="white")
#img1.arc(shape, 90, -90, 'white')
draw = aggdraw.Draw(img)
pen = aggdraw.Pen("white", 1)
#draw.arc([10,10,w-10,h-10], 90, -90, pen)
#draw.flush()
#img.show()

#img2 = img.rotate(45, expand=True)
#img2.show()

mitad = h / 2
pond = 100

def getPen(index):
    color = None
    if(index==0): color = "white"
    if(index==1): color = "red"

    return aggdraw.Pen(color, 1)

for i, a in enumerate(amplitude):
    #new_a = a*10 + 10
    if i > 0:
        draw.line((time[i-1], mitad - round(amplitude[i-1]*pond), time[i], mitad - round(a*pond)), pen)
        #img1.point([time[i], mitad + round(a)*10],'white')
    #draw.line((0, 0, time[i], mitad - round(a)*pond), getPen(i%2))

#draw.line((time[0],mitad + amplitude[0]*pond,time[1],10), pen)

draw.flush()

img.show()
