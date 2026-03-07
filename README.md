HRIT-Consciousness-Simulations
This repository contains the official Python simulations for Hierarchical Recursive Integration Theory (HRIT), a unified neurobiological framework of consciousness. These scripts provide the computational evidence for the transitions between phenomenal tiers and the formal stability metrics proposed in the HRIT manuscript.

Overview
HRIT posits that consciousness is a non-linear product of four specific neural components:HGM (Hierarchical Generative Modeling)CS (Counterfactual Simulation)AFEM (Active Free Energy Minimization)RSR (Recursive Self-Representation)
The core mathematical claim is $C = f(\prod Z_i)$, where consciousness ($C$) is a multiplicative function of these components.

Key Simulations
1. The VPM Principle (Variance-Precedes-Mean)
   Files: The VPM Principle (Early Warning Simulation).py, Stochastic VPM (Critical Slowing Down).py
   These scripts simulate the Critical Slowing Down of the Recursive Stability Index (RSI). They demonstrate how a spike in signal variance (the VPM signature) serves as an early-warning signal for a "dissociative snap" or state-collapse, long before the mean stability drops.
2. Stability Phenotyping
   Files: Stability Phenotyping Radar Chart.py, Clinical Radar Plot Component-Specific Failure.py
   These simulations use polar projections to map clinical disorders (DPDR, Amnesia, Cotard’s) onto the HRIT component space. It illustrates how selective degradation of specific recursive loops creates distinct phenomenal "footprints."
3. The Multiplicative Snap
   Files: The Multiplicative Snap vs. Additive Fade.py, Integration-Weighted Scaling ($f_3$).py
   A visualization of the "Cliff Effect" in HRIT. Unlike additive models where consciousness dims linearly, the HRIT product structure explains why consciousness appears as a discrete, all-or-nothing "snap" into coherence.

Installation & Usage
To run these simulations, you will need Python 3.x and the following libraries:
Bash
pip install numpy matplotlib scipy
Simply run any script to generate the corresponding figure from the paper:
Bash
python "The VPM Principle (Early Warning Simulation).py"
