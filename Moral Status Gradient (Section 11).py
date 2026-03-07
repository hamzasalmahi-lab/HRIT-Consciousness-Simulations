import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Species: (AFEM depth / NIL suffering capacity, RSR depth / self-directed suffering, label)
species = [
    (0.95, 0.95, 'Human\n(adult)'),
    (0.90, 0.70, 'Great Ape\n(chimp/bonobo)'),
    (0.85, 0.55, 'Elephant'),
    (0.82, 0.50, 'Dolphin/\nOrcа'),
    (0.75, 0.35, 'Dog/Wolf'),
    (0.72, 0.30, 'Pig'),
    (0.68, 0.25, 'Crow/\nRaven'),
    (0.60, 0.18, 'Rat/Mouse'),
    (0.55, 0.12, 'Chicken'),
    (0.40, 0.08, 'Fish\n(teleost)'),
    (0.30, 0.04, 'Octopus'),
    (0.18, 0.02, 'Insect'),
    (0.05, 0.01, 'Plant\n(Tier 1)'),
    (0.95, 0.40, 'Human\n(infant <18mo)'),
    (0.95, 0.75, 'Human\n(dementia, severe)'),
]

fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle("HRIT Graded Moral Status: NIL AFEM Depth × RMCL RSR Depth\n(Section 11 — Ethical Gradient)", fontsize=13, fontweight='bold')

afem = np.array([s[0] for s in species])
rsr  = np.array([s[1] for s in species])
moral_score = (afem + rsr) / 2  # composite for color

scatter = ax.scatter(afem, rsr, c=moral_score, cmap='RdYlGn', s=160, alpha=0.88,
                     edgecolors='white', linewidths=1.5, vmin=0, vmax=1, zorder=5)

for (a, r, label) in species:
    offset_x = 0.015
    offset_y = 0.018
    if 'infant' in label or 'dementia' in label:
        offset_y = -0.04
    ax.annotate(label, (a, r), xytext=(a + offset_x, r + offset_y),
                fontsize=8, ha='left', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.65, edgecolor='none'))

# Threshold lines
ax.axhline(0.35, color='grey', linestyle='--', linewidth=1, alpha=0.6)
ax.axvline(0.35, color='grey', linestyle='--', linewidth=1, alpha=0.6)
ax.text(0.37, 0.36, 'RSR threshold\n(self-directed suffering)', fontsize=8, color='grey')
ax.text(0.36, 0.02, 'AFEM threshold\n(basic suffering)', fontsize=8, color='grey')

# Quadrant labels
ax.text(0.08, 0.85, 'High AFEM\nHigh RSR\n(full moral status)', fontsize=8.5,
        ha='center', color='#2E7D32', style='italic',
        bbox=dict(boxstyle='round', facecolor='#E8F5E9', alpha=0.6))
ax.text(0.08, 0.08, 'Low AFEM\nLow RSR\n(minimal moral consideration)', fontsize=8.5,
        ha='center', color='#C62828', style='italic',
        bbox=dict(boxstyle='round', facecolor='#FFEBEE', alpha=0.6))

cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
cbar.set_label('Composite Moral Status Score (HRIT)', fontsize=10)

ax.set_xlabel('NIL AFEM Depth — Capacity for Suffering\n(insular-HPA circuit complexity)', fontsize=11)
ax.set_ylabel('RMCL RSR Depth — Capacity for Self-Directed Suffering\n(mPFC–insula–TPJ metacognitive circuit)', fontsize=11)
ax.set_xlim(0, 1.08)
ax.set_ylim(0, 1.08)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(alpha=0.2, linestyle='--')

plt.tight_layout()
plt.savefig('Moral_Status_Gradient.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()

