# Q1. IMAGE BRIGHTNESS ADJUSTMENT (Broadcasting)
# You are given a grayscale image represented as a 2D NumPy array.
# Increase the brightness of the image by adding a constant value (e.g., +50)
# using broadcasting. Ensure pixel values do not exceed 255.


import numpy as np
image=np.array([[10,20],[30,230]])
bright_image=np.clip(image+50,0,255)
print(bright_image)