from __future__ import division
from numpy import sin, cos, sqrt
from PIL import Image
import numpy as np

# Creating 200 x 200 pixels array object
q2_shape_a = np.zeros((200, 200), dtype=np.uint8)

# Parametric routine: (t) -> tsen(t), tcos(t)
def Y(t):
    return t*sin(t), t*cos(t)

q2_shape_a = np.zeros((200, 200), dtype=np.uint8)
for t in range(0, 1000):
    i, j = Y(t/10)
    i, j = (199-int(i+99), int(j+99))
    q2_shape_a[i][j] = 255
img_y = Image.fromarray(q2_shape_a)
img_y

# Saving image from array of points
Image.fromarray(q2_shape_a).save('q2_a.png')

# Creating 200 x 200 pixels array object
q2_shape_b = np.zeros((200, 200), dtype=np.uint8)


# Implicit function: t -> 1/||y'(t)||
# ||y'(t)|| = sqrt (y'(t))
def Yb(t):
    return 1.0/sqrt((sin(t) + t*cos(t))**2 + (cos(t) - t*sin(t))**2)

t = 0
while t < 100:
    i, j = Y(t)
    i, j = (199-int(i+99), int(j+99))

    # Painting of white points in curve
    q2_shape_b[i][j] = 255
    # Updating t value with function
    t = t + Yb(t)

# Saving image from array of points
Image.fromarray(q2_shape_b).save('q2_b.png')
