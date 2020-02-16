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


def buildGrid(numOfSquares, thickness, inimg, outimg, lower, upper):
	rect = []
	grid = []
	lowerv = np.vectorize(lower)
	dim = inimg.shape
	for i in range(0,numOfSquares):
		for j in range(0,numOfSquares):
			startx = int((dim[0]) * (i/numOfSquares)) + int(thickness/2)
			starty = int((dim[1]) * (j/numOfSquares)) + int(thickness/2)
			endx = int((dim[0]) * ((i + 1)/numOfSquares)) - int(thickness/2)
			endy = int((dim[1]) * ((j + 1)/numOfSquares)) - int(thickness/2)
			
			roi = inimg[starty:endy, startx:endx]
			start = (startx, starty)
			end = (endx, endy)

			if(detectColor(roi)):
				color = np.ndarray.tolist(upper)
			else:
				color = (0,0,0)
			rect = [start, end, color, thickness]
			cv2.rectangle(outimg, start, end, color, thickness)
			grid.append(rect)
	return grid


def detectColor(roi):
	threshold = (roi.shape[0] * roi.shape[1]) * 0.1
	print(threshold)
	gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	nonz = cv2.countNonZero(gray)
	return nonz > threshold


def drawBorder(stack, color, thickness):
	for image in stack:
		start_point = (0,0)
		end_point = (image.shape[0] - thickness, image.shape[1] - thickness)
		image = cv2.rectangle(image, start_point, end_point, color, thickness) 
	return stack


def Reverse(tup):
    for x in tup:
        x.reverse()
    return tup


# define the list of colors
colors = [
    white,
	red,
    yellow,
    blue
]


for boundary in colors:
    #Lists read in reverse (BRG)
    Reverse(boundary)


# loop over the colors
for (lower, upper) in colors:
 	# create NumPy arrays from the colors
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified colors and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	output2 = cv2.bitwise_and(image, image, mask = mask)
	grid = buildGrid(
		squares, 
		4, 
		output,
		output2, 
		lower, 
		upper
		)

	borderColor = (0, 0, 255)
	thickness = 1
	images = [image, output, output2]
	images = drawBorder(images, borderColor, thickness)

	cv2.imshow("images", np.hstack(images))
	cv2.waitKey(0)

# brightLAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# output = cv2.bitwise_and(image, image, mask = mask)

# cv2.imshow("images", np.hstack([image, output]))