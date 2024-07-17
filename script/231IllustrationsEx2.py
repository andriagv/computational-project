import numpy as np
import matplotlib.pyplot as plt


time = np.arange(0, 10, 0.1)
acceleration = np.sin(time)
speed = np.cumsum(acceleration)


vehicle_acceleration = np.gradient(speed, time)


plt.figure(figsize=(10, 5))
plt.plot(time, speed, label='Speed')
plt.plot(time, vehicle_acceleration, label='Acceleration')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Autonomous Driving - Speed and Acceleration')
plt.legend()
plt.grid(True)
plt.show()
