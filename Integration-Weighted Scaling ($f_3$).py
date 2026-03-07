import numpy as np
import matplotlib.pyplot as plt

p_values = np.linspace(0, 1, 100)
f1 = p_values  # Linear
f2 = np.where(p_values > 0.4, p_values, 0)  # Threshold
f3 = p_values * (1 / (1 + np.exp(-10*(p_values-0.5)))) # Sigmoidal Network Binding

plt.figure(figsize=(10, 6))
plt.plot(p_values, f1, 'k--', label='$f_1$: Linear (Minimal)', alpha=0.5)
plt.plot(p_values, f2, 'g:', label='$f_2$: Threshold-Gated', linewidth=2)
plt.plot(p_values, f3, 'b-', label='$f_3$: Integration-Weighted (Binding)', linewidth=3)

plt.title("Candidate Integration Functions for HRIT", fontweight='bold')
plt.xlabel("Global Component Activity ($P$)")
plt.ylabel("Conscious Intensity ($C$)")
plt.legend()
plt.show()
