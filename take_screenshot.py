import numpy as np
import pyautogui
import cv2
from PIL import Image
import imutils

# Capture screenshot using PyAutoGUI
image = pyautogui.screenshot()

# Convert PIL image to OpenCV compatible numpy array
image_np = np.array(image)

# Convert RGB image to BGR (OpenCV uses BGR format)
image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

# Write image to disk using cv2.imwrite()
cv2.imwrite("screenshot.png", image_np)