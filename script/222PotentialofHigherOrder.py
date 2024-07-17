import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
image = np.sin(x) * np.cos(y)


noise = np.random.normal(0, 0.1, size=image.shape)
noisy_image = image + noise


fourth_derivative = gaussian_filter(noisy_image, sigma=1, order=4)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.subplot(1, 2, 2)
plt.imshow(fourth_derivative, cmap='gray')
plt.title('Fourth Derivative (Feature)')
plt.show()
