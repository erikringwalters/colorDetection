import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
ap.add_argument("-r", "--roi", help = "roi of image from center")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
roi = int(args["roi"])

imageDimensions = image.shape

centerx = int(imageDimensions[0] / 2)
centery = int(imageDimensions[1] / 2)
center = (centerx, centery)
print(center)

startx = int(centerx) - int(roi/2)
starty = int(centery) - int(roi/2)
endx = int(centerx) + int(roi/2)
endy = int(centery) + int(roi/2)

roi = image[startx:endx, starty:endy]
cv2.imshow("image", image)
cv2.waitKey(0)

cv2.imshow("roi", roi)

cv2.waitKey(0)

