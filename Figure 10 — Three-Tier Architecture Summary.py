import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis('off')
fig.suptitle("HRIT Tripartite Tier Architecture\nNeural Implementation and Consciousness Equation", fontsize=13, fontweight='bold', y=0.98)

tier_data = [
    {
        'tier': 'Tier 1 — Genomic Autoregulatory Layer (GAL)',
        'subtitle': 'Biochemical self-maintenance · No neural computation',
        'examples': 'Bacteria · Single-celled organisms · Vegetative bodily functions',
        'neural': 'DNA/RNA autoregulation · HPA baseline · Cellular metabolism',
        'components': {'HGM': 0.0, 'CS': 0.0, 'AFEM': 0.0, 'RSR': 0.0},
        'C': 0.0,
        'color': '#D6EAF8',
        'edge': '#2980B9',
        'y': 5.0,
    },
    {
        'tier': 'Tier 2 — Neuroregulatory Integration Layer (NIL)',
        'subtitle': 'Reflexive sensorimotor processing · Thalamocortical circuits',
        'examples': 'Insects · Fish · Reflexive animal behavior · Neonatal brain',
        'neural': 'Brainstem–limbic–thalamic loops · LC-NE · Raphe · PPN',
        'components': {'HGM': 0.55, 'CS': 0.0, 'AFEM': 0.6, 'RSR': 0.0},
        'C': 0.0,
        'color': '#D5F5E3',
        'edge': '#27AE60',
        'y': 3.0,
    },
    {
        'tier': 'Tier 3 — Recursive Metaintegrative Conscious Layer (RMCL)',
        'subtitle': 'Deliberative self-modeling · mPFC–insula–TPJ–hippocampal network',
        'examples': 'Adult humans · Great apes · Cetaceans · Elephants',
        'neural': 'Laminar HGM · Hippocampal CS · Insular AFEM · mPFC–TPJ RSR',
        'components': {'HGM': 0.9, 'CS': 0.85, 'AFEM': 0.85, 'RSR': 0.9},
        'C': 0.88,
        'color': '#EAD8F5',
        'edge': '#7D3C98',
        'y': 1.0,
    },
]

for td in tier_data:
    y = td['y']
    # Main box
    box = FancyBboxPatch((0.3, y - 0.05), 8.5, 1.65,
                         boxstyle="round,pad=0.1", linewidth=2,
                         edgecolor=td['edge'], facecolor=td['color'], zorder=2)
    ax.add_patch(box)
    ax.text(0.6, y + 1.35, td['tier'], fontsize=10.5, fontweight='bold', color=td['edge'], va='top')
    ax.text(0.6, y + 1.05, td['subtitle'], fontsize=8.5, color='#333', va='top', style='italic')
    ax.text(0.6, y + 0.72, f"Examples: {td['examples']}", fontsize=8, color='#555', va='top')
    ax.text(0.6, y + 0.42, f"Neural: {td['neural']}", fontsize=8, color='#333', va='top')

    # Component bars
    comps = td['components']
    bar_x = 9.1
    bar_w = 0.55
    bar_h_max = 0.28
    comp_colors = {'HGM': '#2C5F8A', 'CS': '#6A3D9A', 'AFEM': '#E07B39', 'RSR': '#1A7A4A'}
    for i, (comp, val) in enumerate(comps.items()):
        bx = bar_x + i * (bar_w + 0.12)
        filled_h = val * bar_h_max * 4
        ax.bar(bx, filled_h, width=bar_w, bottom=y + 0.1,
               color=comp_colors[comp], alpha=0.75, zorder=3)
        ax.text(bx + bar_w/2, y - 0.0, comp, ha='center', fontsize=7.5,
                color=comp_colors[comp], fontweight='bold')

    # C value
    c_x = 12.4
    c_r = 0.38
    c_col = td['edge']
    circle = plt.Circle((c_x, y + 0.75), c_r, color=c_col, alpha=0.18, zorder=2)
    ax.add_patch(circle)
    ax.text(c_x, y + 0.85, 'C =', ha='center', fontsize=8.5, color=c_col, va='center')
    ax.text(c_x, y + 0.55, f"{td['C']:.2f}", ha='center', fontsize=11, color=c_col,
            fontweight='bold', va='center')

# Arrows showing tier progression
for y_from, y_to in [(2.75, 4.75), (0.75, 2.75)]:
    ax.annotate('', xy=(4.5, y_to), xytext=(4.5, y_from - 0.05),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))

# Column headers
ax.text(4.5, 6.9, 'Neural Architecture', ha='center', fontsize=9.5, color='#333', style='italic')
ax.text(10.85, 6.9, 'Components', ha='center', fontsize=9.5, color='#333', style='italic')
ax.text(12.4, 6.9, 'C', ha='center', fontsize=9.5, color='#333', style='italic')

# Equation at bottom
ax.text(6.5, 0.15, 'Consciousness = f ( HGM × CS × AFEM × RSR )',
        ha='center', fontsize=11, fontweight='bold', color='#1A3A5C',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#EEF4FB', edgecolor='#2C5F8A', linewidth=1.5))

plt.tight_layout()
plt.savefig('Three_Tier_Architecture.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
