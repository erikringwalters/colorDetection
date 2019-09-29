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

#red = ([100, 15, 17], [200, 56, 50])
#[92, 9, 15] lower limit red

red = ([66, 3, 8], [247, 52, 45])
blue = ([4, 31, 50], [50, 187, 250])
yellow = ([180, 140, 25], [255, 255, 100])
green = ([23, 71, 49], [94, 235, 103])
gray = ([65, 86, 103], [128, 133, 145])
black = ([0, 0, 0], [60, 60, 49])

def Reverse(tup):
    for x in tup:
        x.reverse()
    return tup

# define the list of boundaries
boundaries = [
	red,
	blue,
    yellow,
    green,
    gray,
    black
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

