import numpy as np
import matplotlib.pyplot as plt


image = np.zeros((100, 100))
image[30:70, 40:60] = 1  


plt.imshow(image, cmap='gray')
plt.title('Example of Edges')
plt.axis('off')
plt.show()
