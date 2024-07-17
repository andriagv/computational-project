import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
image = np.sin(x**2 + y**2) 


noise = np.random.normal(0, 0.1, size=image.shape)
noisy_image = image + noise


second_derivative = gaussian_filter(noisy_image, sigma=1, order=2)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.subplot(1, 2, 2)
plt.imshow(second_derivative, cmap='gray')
plt.title('Second Derivative (Edge)')
plt.show()
