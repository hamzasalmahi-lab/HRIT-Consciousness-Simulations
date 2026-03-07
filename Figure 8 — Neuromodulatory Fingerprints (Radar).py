import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

labels = ['Dopamine\n(DA)', 'Norepinephrine\n(NE)', 'Serotonin\n(5-HT)', 'Acetylcholine\n(ACh)', 'GABA\nInterneurons']
N = len(labels)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

states_data = {
    'Healthy Waking':   ([0.85, 0.65, 0.75, 0.60, 0.80], '#1A3A5C'),
    'REM Sleep':        ([0.30, 0.10, 0.50, 0.90, 0.55], '#6A3D9A'),
    'Dissociation':     ([0.45, 0.92, 0.35, 0.40, 0.30], '#E07B39'),
    'Propofol Anesthesia': ([0.20, 0.15, 0.30, 0.10, 0.95], '#888888'),
    'Psychedelic (5-HT2A)': ([0.70, 0.55, 0.15, 0.65, 0.40], '#2E8B57'),
}

fig, axes = plt.subplots(2, 3, figsize=(14, 9), subplot_kw=dict(polar=True))
fig.suptitle("Neuromodulatory Fingerprints Across Consciousness States\n(HRIT Sections 1A.6 and 8)", fontsize=13, fontweight='bold')
axes_flat = axes.flatten()

for idx, (state, (vals, color)) in enumerate(states_data.items()):
    ax = axes_flat[idx]
    vals_plot = vals + vals[:1]
    ax.plot(angles, vals_plot, color=color, linewidth=2.2)
    ax.fill(angles, vals_plot, color=color, alpha=0.22)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['0.25', '0.5', '0.75', '1.0'], fontsize=6.5, color='grey')
    ax.set_title(state, fontsize=10, fontweight='bold', pad=14, color=color)
    ax.grid(alpha=0.3)

# Hide the 6th unused subplot
axes_flat[5].set_visible(False)

plt.tight_layout()
plt.savefig('Neuromodulatory_Fingerprints.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
