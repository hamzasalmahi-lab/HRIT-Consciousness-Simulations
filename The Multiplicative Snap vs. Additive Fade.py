import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define component ranges (0 to 1)
x = np.linspace(0.01, 1, 30)
y = np.linspace(0.01, 1, 30)
X, Y = np.meshgrid(x, y)

# Simulation: Assume two other components are held constant at 0.8
constant_val = 0.8

# HRIT Product Model: C = HGM * CS * AFEM * RSR
C_hrit = X * Y * constant_val * constant_val

# Additive Model: C = (HGM + CS + AFEM + RSR) / 4
C_additive = (X + Y + constant_val + constant_val) / 4

fig = plt.figure(figsize=(14, 6))

# Plot HRIT
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, C_hrit, cmap='viridis', edgecolor='none')
ax1.set_title("HRIT: Multiplicative Snap (Product)")
ax1.set_xlabel('Component A (CS)')
ax1.set_ylabel('Component B (RSR)')
ax1.set_zlabel('Consciousness (C)')

# Plot Additive
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, C_additive, cmap='plasma', edgecolor='none')
ax2.set_title("Standard Models: Additive Fade")
ax2.set_xlabel('Component A')
ax2.set_ylabel('Component B')
ax2.set_zlabel('Consciousness (C)')

plt.tight_layout()
plt.show()
