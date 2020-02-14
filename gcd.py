import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
ap.add_argument("-n", "--numOfSquares", help = "number of rectangles on grid")

args = vars(ap.parse_args())

white = ([130, 130, 130], [255, 255, 255])
red = ([50, 0, 0], [255, 100, 50])
yellow = ([180, 140, 25], [255, 255, 150])
blue = ([4, 60, 50], [80, 130, 255])

# load the image
image = cv2.imread(args["image"])
squares = args["numOfSquares"]

squares = int(squares)

imageDimensions = image.shape


def buildGrid(numOfSquares, thickness, dim):
	rect = []
	grid = []
	for i in range(0,numOfSquares):
		for j in range(0,numOfSquares):
			startx = int((dim[0]) * (i/numOfSquares)) + int(thickness/2)
			starty = int((dim[1]) * (j/numOfSquares)) + int(thickness/2)
			endx = int((dim[0]) * ((i + 1)/numOfSquares)) - int(thickness/2)
			endy = int((dim[1]) * ((j + 1)/numOfSquares)) - int(thickness/2)
			start = (startx, starty)
			end = (endx,endy)
			color = (255,255,255)
			rect = [start, end, color, thickness]
			cv2.rectangle(image, start, end, color, thickness)
			grid.append(rect)
	return grid


def Reverse(tup):
    for x in tup:
        x.reverse()
    return tup

# define the list of boundaries
boundaries = [
    white,
	red,
    yellow,
    blue,

]
grid = buildGrid(squares, 4, imageDimensions)

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
