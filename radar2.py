import matplotlib.pyplot as plt
import numpy as np

# Create a polar plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Simulate static data
angles = np.linspace(0, 2 * np.pi, 100)  # Angles in radians
radii = np.abs(np.sin(angles) * 10)      # Radii based on some function

# Plot the data
ax.plot(angles, radii, label="Static Data")
ax.fill(angles, radii, alpha=0.3)

# Add title
plt.title("Radar Simulation (Static)", va='bottom')
plt.legend()
plt.show()
