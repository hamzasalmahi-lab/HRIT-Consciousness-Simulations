import numpy as np
import matplotlib.pyplot as plt

def simulate_vpm(timesteps=1000):
    t = np.arange(timesteps)
    # Mean stability stays roughly constant then starts to drop at the end
    mean_rsi = np.hstack([np.ones(700) * 0.8, np.linspace(0.8, 0.4, 300)])
    
    # Variance increases as we approach the tipping point (Critical Slowing Down)
    noise_scaling = np.linspace(0.05, 0.4, timesteps)
    noise = np.random.normal(0, noise_scaling, timesteps)
    
    rsi_signal = mean_rsi + noise
    
    # Calculate rolling variance
    window = 50
    rolling_var = [np.var(rsi_signal[max(0, i-window):i]) for i in range(len(rsi_signal))]
    
    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(t, rsi_signal, color='blue', alpha=0.3, label='Raw RSI Signal')
    ax1.plot(t, mean_rsi, color='blue', linewidth=2, label='Mean RSI')
    ax1.set_ylabel('RSI Stability', color='blue')
    ax1.axvline(x=700, color='red', linestyle='--', label='Pro-dromal Instability')

    ax2 = ax1.twinx()
    ax2.plot(t, rolling_var, color='orange', linewidth=2, label='RSI Variance (VPM)')
    ax2.set_ylabel('Variance', color='orange')
    
    plt.title("VPM Principle: Variance Inflation Preceding State Collapse")
    fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
    plt.show()

simulate_vpm()
