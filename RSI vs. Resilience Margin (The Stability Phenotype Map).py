import matplotlib.pyplot as plt

# Clinical Phenotypes
states = {
    "Healthy": (0.85, 0.8),
    "Metabolic Fragility": (0.75, 0.3),  # High RSI, Low Buffer
    "Near-Threshold Instability": (0.45, 0.2),
    "Global Suppression (Anesthesia)": (0.1, 0.1),
    "Fragmented Integration": (0.3, 0.5)
}

plt.figure(figsize=(10, 8))
for label, (rsi, rm) in states.items():
    plt.scatter(rsi, rm, s=200, label=label)
    plt.text(rsi+0.02, rm+0.02, label, fontweight='bold')

plt.axhline(y=0.25, color='gray', linestyle='--') # Resilience Floor
plt.axvline(x=0.4, color='red', linestyle='--')   # RSI Snap Point

plt.title("HRIT State Space: RSI vs. Resilience Margin", fontsize=14)
plt.xlabel("Recursive Stability Index (RSI)")
plt.ylabel("Resilience Margin (RM / Metabolic Buffer)")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(alpha=0.2)
plt.show()
