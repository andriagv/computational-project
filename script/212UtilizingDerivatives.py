import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'example_image.jpg')


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to load image.")
else:
    print("Image loaded successfully!")


sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)


gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_direction = np.arctan2(sobel_y, sobel_x)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gradient_direction, cmap='hsv')
plt.title('Gradient Direction')
plt.axis('off')
plt.show()
