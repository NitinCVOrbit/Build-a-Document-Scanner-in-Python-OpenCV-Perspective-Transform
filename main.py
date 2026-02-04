# It reshapes an image so that a tilted or skewed object appears straight and properly aligned (like looking at it from the front).


# ============================================================
# DOCUMENT SCANNER USING MOUSE POINTS + PERSPECTIVE TRANSFORM
# ============================================================
# STEP 1  : Import required libraries for image processing
# STEP 2  : Load the input image
# STEP 3  : Create an empty list to store mouse click points
# STEP 4  : Define mouse callback function to capture 4 points
# STEP 5  : Draw a small circle on every mouse click
# STEP 6  : After 4 points are selected, apply perspective transform
# STEP 7  : Warp the selected region to a fixed rectangle
# STEP 8  : Convert warped image to HSV color space
# STEP 9  : Extract V (brightness) channel
# STEP 10 : Apply adaptive thresholding on V channel
# STEP 11 : Display perspective transformed image
# STEP 12 : Display thresholded (scanned-like) output
# STEP 13 : Create OpenCV window and set mouse callback  
# STEP 14 : Wait for user interaction
# STEP 15 : Close all OpenCV windows
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_local

# ---------------- Load Image ----------------
img = cv2.imread("01.jpg")
img = cv2.resize(img, (1280, 720))
orig = img.copy()

points = []

# ---------------- Mouse Callback ----------------
def mouse_click(event, x, y, flags, param):
    global points, img

    # Check if left mouse button is clicked and less than 4 points are selected
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:

        # Store clicked (x, y) point
        points.append([x, y])
        print(points)

        # Draw a small red circle at clicked point
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

        # Update window with drawn point
        cv2.imshow("Select Points", img)

        # If 4 points are selected, perform perspective transform
        if len(points) == 4:
            perspective_and_threshold()

# ---------------- Perspective + Threshold ----------------
def perspective_and_threshold():
    # np.float32 → converts points to 32-bit floating values (OpenCV requires this format)
    # points → list of 4 selected corner points from the original image
    pts1 = np.float32(points)


    # width → desired output image width (in pixels)
    # height → desired output image height (in pixels)
    width, height = 300, 400


    # pts2 → destination points where pts1 will be mapped
    # [0, 0] → top-left corner of output image
    # [width, 0] → top-right corner
    # [width, height] → bottom-right corner
    # [0, height] → bottom-left corner
    pts2 = np.float32([
        [0, 0],
        [width, 0],
        [width, height],
        [0, height]
    ])


    # cv2.getPerspectiveTransform →
    # pts1 → source points from original image
    # pts2 → destination points in output image
    # matrix → 3×3 transformation matrix that maps pts1 to pts2
    matrix = cv2.getPerspectiveTransform(pts1, pts2)


    # cv2.warpPerspective →
    # orig → original input image
    # matrix → perspective transformation matrix
    # (width, height) → size of the output image
    # warped → final transformed (top-view) image
    warped = cv2.warpPerspective(orig, matrix, (width, height))

    # # Convert the image to HSV color format
    # # HSV separates color and brightness, which makes processing easier
    # hsv = cv2.cvtColor(warped, cv2.COLOR_BGR2HSV)


    # # Take only the V channel
    # # V means "Value" → how bright each pixel is
    # # Bright pixel = high value, dark pixel = low value
    # V = hsv[:, :, 2]


    # # ---------------- Adaptive Threshold (Very Simple) ----------------
    # # Adaptive threshold means:
    # # "Decide white or black for each pixel based on nearby pixels"
    # # It works well even if the image has shadows or uneven light


    # # Calculate local threshold values
    # # 25 → look at a small 25×25 area around each pixel
    # # offset=15 → slightly lowers the threshold to detect more details
    # # gaussian → nearby pixels matter more than far ones
    # # T → stores the brightness limit for every pixel
    # T = threshold_local(V, 25, offset=15, method="gaussian")


    # # Compare brightness with threshold
    # # If pixel brightness (V) is greater than its local threshold (T)
    # # → pixel becomes white
    # # Else
    # # → pixel becomes black
    # thresh = (V > T).astype("uint8") * 255

        # Convert image to grayscale (required by OpenCV)
    gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(
        gray,                  # input grayscale image
        255,                   # maximum value (white)
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # adaptive method
        cv2.THRESH_BINARY,     # output type (black & white)
        25,                    # block size (local area)
        15                     # constant subtracted from mean
    )

    # ---------------- Display Results ----------------

    # Show warped image
    cv2.imshow("Perspective Transform", warped)
    
    # Show thresholded output
    cv2.imshow('Adaptive Threshold Output', thresh)




# ---------------- Main ----------------

# Create OpenCV window
cv2.namedWindow("Select Points")

# Show original image
cv2.imshow("Select Points", img)

# Attach mouse callback to window
cv2.setMouseCallback("Select Points", mouse_click)

# Instruction message
print("Click 4 points in order: TL → TR → BR → BL")

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
