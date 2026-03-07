import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

age = np.linspace(0, 25, 500)

# RDI: slow early rise, rapid adolescent expansion, plateaus ~22
rdi = np.zeros(500)
for i, a in enumerate(age):
    if a < 1.5:
        rdi[i] = 0.05
    elif a < 4:
        rdi[i] = 0.05 + 0.15 * ((a - 1.5) / 2.5)
    elif a < 12:
        rdi[i] = 0.20 + 0.20 * ((a - 4) / 8)
    elif a < 19:
        rdi[i] = 0.40 + 0.50 * ((a - 12) / 7) ** 0.8   # rapid adolescent surge
    else:
        rdi[i] = 0.90 + 0.10 * (1 - np.exp(-(a - 19) / 2))
rdi = np.clip(rdi, 0, 1.0)

# RSI: rises more slowly, lags RDI through adolescence (neuromodulatory maturation)
rsi = np.zeros(500)
for i, a in enumerate(age):
    if a < 1.5:
        rsi[i] = 0.30
    elif a < 4:
        rsi[i] = 0.30 + 0.10 * ((a - 1.5) / 2.5)
    elif a < 12:
        rsi[i] = 0.40 + 0.15 * ((a - 4) / 8)
    elif a < 22:
        rsi[i] = 0.55 + 0.35 * ((a - 12) / 10) ** 1.4  # slower maturation
    else:
        rsi[i] = 0.90 + 0.10 * (1 - np.exp(-(a - 22) / 1.5))
rsi = np.clip(rsi, 0, 1.0)

# RDI–RSI gap: peak vulnerability
gap = rdi - rsi

fig, axes = plt.subplots(2, 1, figsize=(11, 8), sharex=True)
fig.suptitle("RDI × RSI Developmental Trajectory\nThe Adolescent Instability Window", fontsize=14, fontweight='bold')

# Panel A
ax1 = axes[0]
ax1.plot(age, rdi, color='#E07B39', linewidth=2.5, label='Recursive Depth Index (RDI)')
ax1.plot(age, rsi, color='#2C5F8A', linewidth=2.5, label='Recursive Stability Index (RSI)')
ax1.fill_between(age, rsi, rdi, where=(rdi > rsi), alpha=0.18, color='red', label='Instability window (RDI > RSI)')
ax1.axhline(0.4, color='red', linestyle='--', linewidth=1.3, alpha=0.6, label='RSI threshold (P_th)')

# Milestone annotations
milestones = [(1.5, 'Mirror\nrecognition'), (4, 'Theory\nof mind'), (12, 'Adolescence\nonset'), (22, 'Full\nmaturation')]
for x, label in milestones:
    ax1.axvline(x, color='grey', linestyle=':', alpha=0.5, linewidth=1)
    ax1.text(x, 1.03, label, ha='center', fontsize=8, color='grey',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='grey', alpha=0.7))

ax1.set_ylabel('Index Value (0–1)', fontsize=11)
ax1.set_ylim(0, 1.12)
ax1.legend(loc='upper left', fontsize=9)
ax1.set_title('A. RDI and RSI across development', fontsize=11, loc='left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Panel B: Gap = vulnerability
ax2 = axes[1]
ax2.fill_between(age, gap, 0, where=(gap > 0), alpha=0.4, color='red')
ax2.plot(age, np.clip(gap, 0, 1), color='darkred', linewidth=2.2, label='RDI – RSI gap (vulnerability)')
ax2.axhline(0, color='black', linewidth=0.8)

peak_gap_idx = np.argmax(gap)
ax2.annotate(f'Peak vulnerability\n~age {age[peak_gap_idx]:.0f}',
             xy=(age[peak_gap_idx], gap[peak_gap_idx]),
             xytext=(age[peak_gap_idx] + 2, gap[peak_gap_idx] + 0.04),
             fontsize=9.5, color='darkred', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='darkred', lw=1.3))

ax2.set_xlabel('Age (years)', fontsize=11)
ax2.set_ylabel('RDI – RSI Gap', fontsize=11)
ax2.set_title('B. Instability gap — predicts peak onset of dissociative and psychotic disorders', fontsize=11, loc='left')
ax2.legend(loc='upper right', fontsize=9)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='y', alpha=0.25, linestyle='--')

plt.tight_layout()
plt.savefig('RDI_RSI_Developmental_Trajectory.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
