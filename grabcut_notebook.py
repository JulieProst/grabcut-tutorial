#%% Import all necessary libraries and data
from pathlib import Path

import cv2
from matplotlib import pyplot as plt

IMAGES_FOLDER = Path(__file__).resolve().parents[0] / "images"


def show_image(image, title=None):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])
    plt.title(title)
    plt.show()


#%% Show original image
cat_image = cv2.imread(str(IMAGES_FOLDER / "cute_cat_on_white_background.jpeg"))
show_image(cat_image, "Original Image")

#%% Use OpenCV findContours method
gray_cat = cv2.cvtColor(cat_image, cv2.COLOR_RGB2GRAY)
show_image(gray_cat, "Gray image")

thresh = cv2.adaptiveThreshold(
    gray_cat,
    maxValue=255,
    adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    thresholdType=cv2.THRESH_BINARY,
    blockSize=9,
    C=7,
)
show_image(thresh, "Binarized Image")
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_image = cv2.drawContours(cat_image.copy(), contours, -1, (0, 255, 0), 1)
show_image(contours_image, "Extracted contours")
#%% Run GrabCut

#%% Other segmentation algo ?
