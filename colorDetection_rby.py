# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:03:47 2019

@author: Erik
"""
# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])


# orange = ([150, 0, 0],[250, 100, 50])
# darkGreen = ([0, 50, 30],[50, 80, 60])
# black = ([0, 0, 0], [60, 60, 49])
# brown = ([100, 30, 40],[150, 80, 60])
# green = ([25, 100, 19], [106, 208, 80])
# purple = ([75, 0, 50],[150, 50, 150])
#gray = ([65, 86, 103], [128, 133, 145])

white = ([130, 130, 130], [255, 255, 255])
red = ([50, 0, 0], [255, 70, 50])
yellow = ([180, 140, 25], [255, 255, 150])
blue = ([4, 60, 50], [80, 130, 255])



def Reverse(tup):
    for x in tup:
        x.reverse()
    return tup

# define the list of boundaries
boundaries = [
    white,
	red,
	# orange,
    # darkGreen,
    # black,
    # brown,
    # green,
    yellow,
    # purple,
    blue,
 #   gray,

]

for boundary in boundaries:
    #Lists read in reverse (BRG)
    Reverse(boundary)


# loop over the boundaries
for (lower, upper) in boundaries:
 	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)

# brightLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

output = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)


