import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_precision_gain():
    x = np.linspace(-5, 10, 500)
    prior = norm.pdf(x, 0, 1.5) # Vague prior
    sensory_input = norm.pdf(x, 5, 1.0) # Sensory observation at x=5
    
    # High Precision (Optimal Attention)
    posterior_high = norm.pdf(x, 4, 0.4)
    # Low Precision (Dampened Gain/NIL State)
    posterior_low = norm.pdf(x, 1, 1.2)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, prior, 'gray', linestyle='--', label='Prior (Top-Down)')
    plt.plot(x, sensory_input, 'black', label='Sensory Input (Bottom-Up)')
    
    plt.fill_between(x, posterior_high, color='green', alpha=0.4, label='High Precision (Tier 3 Consciousness)')
    plt.fill_between(x, posterior_low, color='red', alpha=0.4, label='Low Precision (Tier 2/NIL)')
    
    plt.title("Neuromodulatory Gain: Precision-Weighting of the Inferential Field")
    plt.xlabel("State Space")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.show()

simulate_precision_gain()
