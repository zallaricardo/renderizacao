from __future__ import division
from numpy import sin, cos, sqrt
from PIL import Image
import numpy as np

# QUESTION 1

### PARAMETRIC CIRCLE ###

# Creating 200 x 200 pixels array object
q1_shape_parametric = np.zeros((200,200), dtype = np.uint8)

# Parametric routine: (t) -> cos(t), sen(t)
def parametric_circle(t):
    return (cos(t), sin(t))

# Circle points definition and painting loop
for t in range(0,360): # for all angles
    # Creating parametric floating point
    i,j = parametric_circle(t * np.pi/180)

    # Defining x and y coordinates
    i = int(i*100 + 99)
    j = int(j*100 + 99)

    # Defining color of the point
    q1_shape_parametric[i][j] = 255

# Saving image from array of points
Image.fromarray(q1_shape_parametric).save('q1_parametric.png')

### IMPLICIT CIRCLE ###

# Creating 200 x 200 pixels array object
q1_shape_implicit = np.zeros((200,200), dtype=np.uint8)

# Implicit routine: (x,y) -> x^2 + y^2-1
def implicit_circle(x,y):
    return x**2 + y**2 - 1

for x in range(0,200):
    for y in range(0,200):
        # For each point

        # X coordinate edges
        Xf = (x-0.5-100)/100
        Yf = (y-100)/100
        edge_x_in = implicit_circle(Xf,Yf)

        Xf = (x+0.5-100)/100
        Yf = (y-100)/100
        edge_x_out = implicit_circle(Xf,Yf)

        # Y coordinate edges
        Xf = (x-100)/100
        Yf = (y-0.5-100)/100
        edge_y_in = implicit_circle(Xf,Yf)

        Xf = (x-100)/100
        Yf = (y+0.5-100)/100
        edge_y_out = implicit_circle(Xf,Yf)

        # If at least one value has different signals between x or y edges, the point is at the circle
        outside_test = edge_x_in > 0 and edge_x_out > 0 and edge_y_in > 0 and edge_y_out > 0 # positive test - all outside circle
        inside_test = edge_x_in < 0 and edge_x_out < 0 and edge_y_in < 0 and edge_y_out < 0 # negative test - all inside circle
        if  not (outside_test or inside_test): # positive and negative failed
            # Defining color for implicit points
            q1_shape_implicit[199-x][y] = 255

# Saving image from array of points
Image.fromarray(q1_shape_implicit).save('q1_implicit.png')
