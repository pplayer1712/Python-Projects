#function to get all differeces between two images
import cv2

from PIL import Image
from PIL import ImageChops
from PIL import ImageDraw
from debugpy import connect
from imutils import contours
from pyparsing import line_end
from skimage import measure

from tkinter import filedialog as fd

import numpy as np

img1 = fd.askopenfilename(title="Select first image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
img2 = fd.askopenfilename(title="Select second image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])

if img1 == None or img2 == None:
    print("No image selected")
    exit()

diff = ImageChops.difference(Image.open(img2), Image.open(img1))
diff.save(".temp.diff.png", "PNG")

# Get the coordinates of groups of pixels that are not black
gray = cv2.cvtColor(cv2.imread(".temp.diff.png"), cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow("Diff", thresh)
# cv2.waitKey(0)

# perform a connected component analysis on the thresholded
IMG = cv2.imread(img1)
output = cv2.connectedComponentsWithStats(thresh, 8, cv2.CV_32S)
(numLabels, labels, stats, centroids) = output
for i in range(1, numLabels):
	if i == 0:
		text = "examining component {}/{} (background)".format(
			i + 1, numLabels)
	else:
		text = "examining component {}/{}".format( i, numLabels-1)
	print("[INFO] {}".format(text))
	w = stats[i, cv2.CC_STAT_WIDTH]
	h = stats[i, cv2.CC_STAT_HEIGHT]
	area = stats[i, cv2.CC_STAT_AREA]
	(cX, cY) = centroids[i]
	output = thresh.copy()
	cv2.circle(img=IMG, center=(int(cX), int(cY)), radius=max(w,h), color=(0, 0, 255), lineType=-1, thickness=2)

	componentMask = (labels == i).astype("uint8") * 255

cv2.imshow("Connected Component", IMG)
cv2.waitKey(0)
# Save the image
save_path = fd.asksaveasfilename(title="Save image", filetypes=[("Image files", "*.png")])
cv2.imwrite(save_path + ".png", IMG)