import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

np.random.seed(42)
t = np.linspace(0, 100, 1000)
collapse_point = 650  # index ~65% through

# RSI mean: stable, then declining
rsi_mean = np.ones(1000) * 0.75
rsi_mean[collapse_point:] = 0.75 - 0.65 * (1 - np.exp(-(t[collapse_point:] - t[collapse_point]) / 8))
rsi_mean = np.clip(rsi_mean, 0.05, 1.0)

# RSI variance: starts rising BEFORE mean drops (VPM principle)
variance_onset = 520  # index ~52% through — earlier than collapse
rsi_var = np.ones(1000) * 0.03
rsi_var[variance_onset:collapse_point] = 0.03 + 0.18 * ((t[variance_onset:collapse_point] - t[variance_onset]) / (t[collapse_point] - t[variance_onset]))**1.5
rsi_var[collapse_point:] = 0.21 * np.exp(-(t[collapse_point:] - t[collapse_point]) / 12) + 0.03
rsi_var = np.clip(rsi_var, 0, 0.25)

# Add noise to mean for realism
noise = np.random.normal(0, rsi_var * 0.4, 1000)
rsi_signal = rsi_mean + noise

# Alpha-band variance (early warning)
alpha_var = np.ones(1000) * 0.05
alpha_var[variance_onset - 80:collapse_point] = 0.05 + 0.30 * ((t[variance_onset - 80:collapse_point] - t[variance_onset - 80]) / (t[collapse_point] - t[variance_onset - 80]))**1.2
alpha_var[collapse_point:] = 0.35 * np.exp(-(t[collapse_point:] - t[collapse_point]) / 15) + 0.05

fig, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
fig.suptitle("The Variance-Precedes-Mean (VPM) Principle\nNeural Early Warning of RSI Instability", fontsize=14, fontweight='bold', y=0.98)

# Panel A: RSI signal with noise
ax1 = axes[0]
ax1.plot(t, rsi_signal, color='#2C5F8A', alpha=0.6, linewidth=0.8, label='RSI (trial-to-trial)')
ax1.plot(t, rsi_mean, color='#1A3A5C', linewidth=2.2, label='RSI mean')
ax1.axhline(0.4, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='RSI threshold (P_th)')
ax1.axvspan(t[variance_onset], t[collapse_point], alpha=0.08, color='orange', label='VPM window')
ax1.axvline(t[collapse_point], color='red', linestyle='-', linewidth=1.2, alpha=0.5)
ax1.set_ylabel('RSI Level', fontsize=11)
ax1.set_ylim(-0.05, 1.1)
ax1.legend(loc='upper right', fontsize=9)
ax1.set_title('A. RSI Signal and Mean Trajectory', fontsize=11, loc='left')
ax1.annotate('Conscious collapse', xy=(t[collapse_point], 0.4), xytext=(t[collapse_point]+4, 0.6),
             fontsize=9, color='red', arrowprops=dict(arrowstyle='->', color='red', lw=1.2))

# Panel B: RSI variance (VPM signal)
ax2 = axes[1]
ax2.fill_between(t, rsi_var, alpha=0.35, color='#E07B39')
ax2.plot(t, rsi_var, color='#E07B39', linewidth=2, label='RSI trial-to-trial variance')
ax2.axvspan(t[variance_onset], t[collapse_point], alpha=0.08, color='orange')
ax2.axvline(t[variance_onset], color='darkorange', linestyle=':', linewidth=2, label='Variance onset (early warning)')
ax2.axvline(t[collapse_point], color='red', linestyle='-', linewidth=1.2, alpha=0.5)
ax2.set_ylabel('RSI Variance', fontsize=11)
ax2.legend(loc='upper left', fontsize=9)
ax2.set_title('B. RSI Variance — Rises Before Mean Decline', fontsize=11, loc='left')
ax2.annotate(f'Δt = {t[collapse_point]-t[variance_onset]:.0f} AU\nearly warning window', 
             xy=((t[variance_onset]+t[collapse_point])/2, 0.12),
             ha='center', fontsize=9, color='darkorange',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='darkorange', alpha=0.8))

# Panel C: Alpha-band variance
ax3 = axes[2]
ax3.fill_between(t, alpha_var, alpha=0.25, color='#6A3D9A')
ax3.plot(t, alpha_var, color='#6A3D9A', linewidth=2, label='Alpha-band power variance')
ax3.axvspan(t[variance_onset-80], t[collapse_point], alpha=0.08, color='purple')
ax3.axvline(t[variance_onset-80], color='purple', linestyle=':', linewidth=2, label='Alpha variance onset (earliest signal)')
ax3.axvline(t[collapse_point], color='red', linestyle='-', linewidth=1.2, alpha=0.5, label='Conscious collapse')
ax3.set_ylabel('Alpha Variance', fontsize=11)
ax3.set_xlabel('Time (arbitrary units — trial sequence)', fontsize=11)
ax3.legend(loc='upper left', fontsize=9)
ax3.set_title('C. Alpha-Band Variance — Earliest Detectable Warning', fontsize=11, loc='left')

for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.25, linestyle='--')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('VPM_TimeSeries_Figure.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
