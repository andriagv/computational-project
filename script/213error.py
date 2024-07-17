import numpy as np
import matplotlib.pyplot as plt


def finite_difference_derivative(f, x, h):
    return (f(x + h) - f(x)) / h


def sharp_edge_function(x):
    return np.where(x >= 0, 1, 0)


x_values = np.linspace(-1, 1, 1000)

h_values = [0.1, 0.01, 0.001]
derivatives = [finite_difference_derivative(sharp_edge_function, x_values, h) for h in h_values]


plt.figure(figsize=(10, 5))
for i, (h, derivative) in enumerate(zip(h_values, derivatives), 1):
    plt.subplot(1, len(h_values), i)
    plt.plot(x_values, derivative)
    plt.title(f'Step Size: {h}')
plt.suptitle('Effect of Truncation Error on Derivative')
plt.tight_layout()
plt.show()
