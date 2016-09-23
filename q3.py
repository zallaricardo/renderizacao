from __future__ import division
from numpy import sin, cos, sqrt
from PIL import Image
import numpy as np


### QUESTION 3

# Creating 200 x 200 pixels array object
q3_shape = np.zeros((200, 200), dtype=np.uint8)


# Implicit routine: (x,y) ->
#  x + y > 1; and
# (x, y) belongs to circle with r=1 and center (0,1); and
# (x, y) belongs to circle with r=1 and center (1,0).
def U(x, y):
    if (x + y) > 1 and (x**2 + (y-1)**2) < 1 and ((x-1)**2 + y**2) < 1:
        return 0
    else:
        return 1

for x in range(0, 200):
    for y in range(0, 200):
        # Normalize point to respect the window and test if it belongs to U
        if U(x/200, y/200) == 0:
            # Defining color for points in curve
            q3_shape[199-x][y] = 255

# Saving image from array of points
Image.fromarray(q3_shape).save('q3.png')
