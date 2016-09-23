from __future__ import division
from numpy import sin, cos, sqrt
from PIL import Image
import numpy as np

def U_implicit(x,y):
    if (x + y) > 1 and (x**2 + (y-1)**2) < 1 and ((x-1)**2 + y**2) < 1:
        return 0
    else:
        return 1

U_implicit_rast = np.zeros((200,200), dtype=np.uint8)
for x in range(0,200):
    for y in range(0,200):
        x_f = x/200
        y_f = y/200
        z = U_implicit(x_f,y_f)
        if  z == 0:
            U_implicit_rast[199-x][y] = 255

img_U_implicit = Image.fromarray(U_implicit_rast)
img_U_implicit.save('q3.png')
