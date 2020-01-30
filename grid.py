import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])

dim = image.shape

window_name = 'Image'

row = [-1,-1,-1]

# blocks = np.array([row, row, row], np.int32) 
blocks = row
print(blocks)

for i in range(0,3):
    for j in range(0,3):
        start = (0,0)
        endx = int((dim[0]) * ((i + 1)/3))
        endy = int((dim[1]) * ((j + 1)/3))
        end = (endx,endy)
        color = (200, 0, 0)
        thickness = 5

        print(start, end, color, thickness)

        cv2.rectangle(image, start, end, color, thickness)


cv2.imshow(window_name, image)  
cv2.waitKey(0)