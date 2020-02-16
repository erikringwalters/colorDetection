import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
ap.add_argument("-a", "--area", help = "area of square from center of image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
area = int(args["area"])

imageDimensions = image.shape

centerx = int(imageDimensions[0] / 2)
centery = int(imageDimensions[1] / 2)
center = (centerx, centery)
print(center)

startx = int(centerx) - int(area)
starty = int(centery) - int(area)
endx = int(centerx) + int(area)
endy = int(centery) + int(area)

start = (startx, starty)
end = (endx, endy)

area = image[startx:endx, starty:endy]
cv2.imshow("image", image)
cv2.waitKey(0)

cv2.imshow("area", area)

cv2.waitKey(0)

