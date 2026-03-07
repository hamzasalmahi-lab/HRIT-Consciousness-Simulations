import numpy as np
import matplotlib.pyplot as plt

states = ['Waking', 'REM\nDreaming', 'NREM\nLight', 'Slow-Wave\nSleep']
components = ['HGM', 'CS', 'AFEM', 'RSR']

# Component scores per state (0–1) based on HRIT Section 8 descriptions
scores = np.array([
    # HGM   CS     AFEM   RSR
    [0.90,  0.85,  0.85,  0.90],   # Waking
    [0.75,  0.88,  0.55,  0.60],   # REM: high CS (replay), reduced AFEM/RSR (NE withdrawal)
    [0.55,  0.40,  0.40,  0.35],   # NREM Light: partial integration
    [0.20,  0.10,  0.15,  0.05],   # SWS: global suppression, near-zero RSR
])

rsi_scores = [0.88, 0.62, 0.38, 0.08]
colors = ['#1A3A5C', '#6A3D9A', '#2E8B57', '#888888']

fig, axes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("HRIT Component Profiles Across Sleep States", fontsize=14, fontweight='bold')

# Panel A: Grouped bar chart
ax1 = axes[0]
x = np.arange(len(components))
width = 0.18
for i, (state, color) in enumerate(zip(states, colors)):
    bars = ax1.bar(x + i * width, scores[i], width, label=state, color=color, alpha=0.82, edgecolor='white')

ax1.axhline(0.4, color='red', linestyle='--', linewidth=1.3, alpha=0.7, label='RSI threshold (P_th)')
ax1.set_xticks(x + 1.5 * width)
ax1.set_xticklabels(components, fontsize=12)
ax1.set_ylabel('Component Score (0–1)', fontsize=11)
ax1.set_ylim(0, 1.1)
ax1.legend(fontsize=9, loc='upper right')
ax1.set_title('A. Component-level scores by sleep state', fontsize=11, loc='left')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Panel B: RSI composite by state
ax2 = axes[1]
bars2 = ax2.barh(states, rsi_scores, color=colors, alpha=0.82, edgecolor='white', height=0.5)
ax2.axvline(0.4, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='RSI threshold')

for bar, score in zip(bars2, rsi_scores):
    ax2.text(score + 0.01, bar.get_y() + bar.get_height()/2, f'{score:.2f}',
             va='center', fontsize=10, fontweight='bold')

ax2.annotate('', xy=(0.4, -0.6), xytext=(0, -0.6),
             arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
ax2.text(0.2, -0.85, 'Below\nthreshold', ha='center', color='red', fontsize=8.5)

ax2.set_xlabel('Composite RSI Score', fontsize=11)
ax2.set_title('B. RSI composite score per state', fontsize=11, loc='left')
ax2.set_xlim(0, 1.15)
ax2.legend(fontsize=9)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('Sleep_Stage_Consciousness_Profile.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
