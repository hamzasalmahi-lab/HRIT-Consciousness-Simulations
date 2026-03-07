import numpy as np
import matplotlib.pyplot as plt

labels = ['HGM (Logic)', 'CS (Time)', 'AFEM (Body)', 'RSR (Self)']
num_vars = len(labels)

# Define phenotypes
healthy = [0.9, 0.8, 0.9, 0.8]
amnesia = [0.8, 0.1, 0.8, 0.7] # Collapsed Counterfactual Simulation (CS)
depersonalization = [0.8, 0.7, 0.6, 0.1] # Collapsed Recursive Self (RSR)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1] # Close the circle

def add_to_radar(data, label, color):
    values = data + data[:1]
    ax.plot(angles, values, color=color, linewidth=2, label=label)
    ax.fill(angles, values, color=color, alpha=0.25)

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

add_to_radar(healthy, "Healthy Tier 3", "green")
add_to_radar(amnesia, "Amnesia (CS Failure)", "blue")
add_to_radar(depersonalization, "DPD (RSR Failure)", "red")

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_thetagrids(np.degrees(angles[:-1]), labels)
plt.title("HRIT Stability Phenotyping: Component-Specific Collapse")
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()
