from PIL import Image


# Imagem inputed
img_input = Image.open('14-bis.jpg')
img_input = img_input.convert("RGBA")

# Image texture
img_text = Image.open('model.jpg')
img_text = img_text.convert("RGBA")


# H transformation routine *generated with outsource*
def transform(x, y):
    H = [[9.32053, 4.17325, -3203.52],
         [2.2457, 10.56666, -1206.89],
         [0.000507563, 0.000800929, 0.799446]
         ]

# New coordinates for each transformed (x,y,z) point
    new_x = H[0][0]*x + H[0][1]*y + H[0][2]*1
    new_Y = H[1][0]*x + H[1][1]*y + H[1][2]*1
    new_Z = H[2][0]*x + H[2][1]*y + H[2][2]*1

# Normalization (z=1)
    new_x = new_x/new_Z
    new_Y = new_Y/new_Z

# Pick the closest pixel point
    return [round(new_x, 0), round(new_Y, 0)]


# Routine to test if the transformed image is completely inside the photo
def isInside(smallX, smallY, bigX, bigY):
    if (smallX > 0 and smallY > 0) and (smallX < bigX and smallY < bigY):
        return True
    return False

# For each point from the original picture
for x in range(img_input.size[0]):
    for y in range(img_input.size[1]):
        [Xt, Yt] = transform(x, y)

        if isInside(Xt, Yt, img_text.size[0], img_text.size[1]) is True:
            color = img_text.getpixel((Xt, Yt))
            img_input.putpixel((x, y), color)

# Saving new image
img_input.save('transformed.png')
