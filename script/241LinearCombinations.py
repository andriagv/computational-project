import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'example_image.jpg')


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


if image is None:
    print("Error: Unable to load image.")
    exit()


sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)


alpha = 0.5
beta = 0.5

# Combine derivatives using linear combination
edge_detection = alpha * sobel_x + beta * sobel_y

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(edge_detection, cmap='gray')
plt.title('Edge Detection (Linear Combination)')
plt.axis('off')
plt.show()
