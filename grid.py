import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
image = cv2.imread(args["image"])

dim = image.shape

window_name = 'Image'

start = (0,0)
endx = int(dim[0]/3)
endy = int(dim[1]/3)
end = (endx,endy)
color = (200, 0, 0)
thickness = 5

cv2.rectangle(image, start, end, color, thickness)

cv2.imshow(window_name, image)  
cv2.waitKey(0)