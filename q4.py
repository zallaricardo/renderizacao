from __future__ import division
from numpy import sin, cos, sqrt
from PIL import Image
import numpy as np

# Creating 200 x 200 pixels array object
q4_shape = np.zeros((200,200), dtype=np.uint8)

# Implicit routine: (x,y) -> y^2 - x^3 + x
def F(x,y):
    return y**2 - x**3 + x

for x in range(0,200):
    for y in range(0,200):
        Xf = (x-0.5-100)/50
        Yf = (y-100)/50
        z1 = F(Xf,Yf)

        Xf = (x+0.5-100)/50
        Yf = (y-100)/50
        z2 = F(Xf,Yf)

        Xf = (x-100)/50
        Yf = (y-0.5-100)/50
        z3 = F(Xf,Yf)

        Xf = (x-100)/50
        Yf = (y+0.5-100)/50
        z4 = F(Xf,Yf)

        all_pos = z1 > 0 and z2 > 0 and z3 > 0 and z4 > 0
        all_neg = z1 < 0 and z2 < 0 and z3 < 0 and z4 < 0

        # Defining color of points in F
        if  not (all_pos or all_neg):
            q4_shape[199-y][x] = 255

# Saving image from array of points
Image.fromarray(q4_shape).save('q4.png')
