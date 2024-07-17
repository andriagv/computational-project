import numpy as np
import matplotlib.pyplot as plt


time = np.arange(0, 10, 0.1)
stock_price = np.sin(time) + np.random.normal(0, 0.1, size=len(time))


rate_of_change = np.gradient(stock_price, time)


plt.figure(figsize=(10, 5))
plt.plot(time, stock_price, label='Stock Price')
plt.plot(time, rate_of_change, label='Rate of Change')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Financial Analysis - Stock Price and Rate of Change')
plt.legend()
plt.grid(True)
plt.show()
