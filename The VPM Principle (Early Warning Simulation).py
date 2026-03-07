import numpy as np
import matplotlib.pyplot as plt

# Generate a time series approaching a "Snap"
t = np.linspace(0, 100, 500)
# Mean stays stable until the very end
mean_rsi = np.where(t < 80, 0.8, 0.8 - 0.03 * (t-80)**2)
# Variance increases linearly as t approaches 80
variance = np.where(t < 80, 0.02 + 0.005 * t, 0.4)
noise = np.random.normal(0, variance)
rsi_signal = mean_rsi + noise

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(t, rsi_signal, color='black', alpha=0.4, label='Raw RSI Signal')
ax1.plot(t, mean_rsi, color='blue', linewidth=2, label='Mean RSI')
ax1.set_ylabel('Recursive Stability Index (RSI)')
ax1.set_xlabel('Time / Stress Load')

ax2 = ax1.twinx()
rolling_var = [np.var(rsi_signal[max(0, i-20):i+1]) for i in range(len(t))]
ax2.plot(t, rolling_var, color='red', linewidth=2, label='VPM Variance (Biomarker)')
ax2.set_ylabel('Neural Variability (Variance)', color='red')

plt.title("Variance-Precedes-Mean (VPM): The Early Warning Signal of Dissociation", fontweight='bold')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
