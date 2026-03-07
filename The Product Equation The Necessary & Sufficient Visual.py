import numpy as np
import matplotlib.pyplot as plt

# Simulate component levels (0 to 1)
x = np.linspace(0, 1, 100)
# Fixed high values for 3 components, 1 variable component
fixed = 0.9

plt.figure(figsize=(10, 6))
plt.plot(x, fixed * fixed * fixed * x, label='Product Integration (HRIT)', color='blue', linewidth=3)
plt.plot(x, (fixed + fixed + fixed + x)/4, '--', label='Additive Integration (GWT/IIT-like)', color='gray')

plt.axvline(x=0.2, color='red', linestyle=':', label='Dissociative Threshold')
plt.fill_between(x, 0, 1, where=(x < 0.2), color='red', alpha=0.1)

plt.title("The HRIT Product Equation: The Geometry of Collapse", fontweight='bold')
plt.xlabel("Strength of any Single Component (HGM, CS, AFEM, or RSR)")
plt.ylabel("Total Conscious Integration ($C$)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
