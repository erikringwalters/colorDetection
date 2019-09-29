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


blue = ( [0, 0, 0], [250, 0, 0])

# red = ([17, 15, 100], [50, 56, 200])
#blue = ([86, 31, 4], [220, 88, 50])
# yellow = ([25, 146, 190], [62, 174, 250])
# gray = ([103, 86, 65], [145, 133, 128])



# define the list of boundaries
boundaries = [
	# red,
	blue
    # yellow,
    # gray
]

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

