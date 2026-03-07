import numpy as np
import matplotlib.pyplot as plt

categories = ['HGM\n(Laminar)', 'CS\n(Hippocampal)', 'AFEM\n(Insular)', 'RSR\n(mPFC)']
N = len(categories)

# Component scores (0-1) for phenotypes
healthy = [0.9, 0.9, 0.9, 0.9]
cotard = [0.8, 0.8, 0.1, 0.7]  # AFEM Collapse [cite: 239]
dissociation = [0.7, 0.6, 0.7, 0.2] # RSR Collapse [cite: 527]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

for data, label, color in zip([healthy, cotard, dissociation], 
                             ['Healthy', "Cotard's", 'Dissociation'], 
                             ['green', 'red', 'purple']):
    values = data + data[:1]
    ax.plot(angles, values, linewidth=2, label=label, color=color)
    ax.fill(angles, values, color=color, alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
plt.title("HRIT Clinical Differential: Component Failure Modes", y=1.1, fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()
