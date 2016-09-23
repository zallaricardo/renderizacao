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
        # For each point

        # X coordinate edges
        Xf = (x-0.5-100)/50
        Yf = (y-100)/50
        edge_x_in = F(Xf,Yf)

        Xf = (x+0.5-100)/50
        Yf = (y-100)/50
        edge_x_out = F(Xf,Yf)

        # Y coordinate edges
        Xf = (x-100)/50
        Yf = (y-0.5-100)/50
        edge_y_in = F(Xf,Yf)

        Xf = (x-100)/50
        Yf = (y+0.5-100)/50
        edge_y_out = F(Xf,Yf)

        # If at least one value has different signals between x or y edges, the point is at the circle
        outside_test = edge_x_in > 0 and edge_x_out > 0 and edge_y_in > 0 and edge_y_out > 0 # positive test - all outside circle
        inside_test = edge_x_in < 0 and edge_x_out < 0 and edge_y_in < 0 and edge_y_out < 0 # negative test - all inside circle
        if  not (outside_test or inside_test): # positive and negative failed
            # Defining color for implicit points
            q4_shape[199-y][x] = 255

# Saving image from array of points
Image.fromarray(q4_shape).save('q4.png')
