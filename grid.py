import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])

dim = image.shape

window_name = 'Image'

thickness = 4


for i in range(0,3):
    for j in range(0,3):
        startx = int((dim[0]) * ((i)/3)) + int(thickness/2)
        starty = int((dim[1]) * ((j)/3)) + int(thickness/2)
        endx = int((dim[0]) * ((i + 1)/3)) - int(thickness/2)
        endy = int((dim[1]) * ((j + 1)/3)) - int(thickness/2)
        start = (startx, starty)
        end = (endx,endy)
        color = (i*75, 0, j*75)

        # print(start, end, color, thickness)

        cv2.rectangle(image, start, end, color, thickness)


cv2.imshow(window_name, image)  
cv2.waitKey(0)