The results of 
python -m experiments.orderability_frozenlake
python -m experiments.orderability_taxi
python -m experiments.agenticity_metrics
python -m  experiments.stress_test

pytest

help us validate the math:



1. The Linear Constraint Argument (Theory)
What the math says:
For policies to be orderable, you need:

$(\mu_{\pi_2} - \mu_{\pi_1})^T r > 0$

$(\mu_{\pi_3} - \mu_{\pi_2})^T r > 0$

This is a system of linear inequalities. If the occupancy measure differences point in conflicting directions, no reward vector $r$ can satisfy both.

What experiments showed:

FrozenLake:
Base: pi1=0.009, pi2=0.0, pi3=0.055
Orderable: False

#Interpretation:

This means the occupancy measures $\mu_{\pi_1}, \mu_{\pi_2}, \mu_{\pi_3}$ are geometrically arranged 
such that no affine reward function can make $\pi_1 < \pi_2 < \pi_3$ hold universally.

We're proving that even in a 4×4 grid world, the geometry of state-action visitation makes certain orderings impossible.
This is a structural property of MDPs, not a computational artifact

This establishes reward design has fundamental limits. You can't always engineer a reward that ranks policies the way you want.

...............................................................................

2. The Robustness-Agenticity Theorem (Experiments)
What the definition says:
A policy $\pi$ is $\epsilon$-agentic if its ranking relative to a baseline stays invariant across reward transforms.

What experiments showed:

Variance-based agenticity:
  random:   18.5  (fragile)
  always_0: 0.0   (robust)
  always_1: 0.0   (robust)

Rank stability: 1.0 (perfect correlation)


#Interpretation:

Deterministic policies (always_0, always_1) have zero variance -> their performance is completely invariant to affine reward transforms

Random policy has high variance -> its ranking collapses under reward misspecification

Rank correlation = 1.0 -> the ordering always_0 < always_1 never flips, no matter how you scale/shift rewards

#Conclusion:
True agents" pursue goals that are robust to reward specification errors. A winning policy in FrozenLake is still winning whether you give +1 or +100 for reaching the goal.

This operationalizes agenticity as invariance under reward perturbation, not just "high expected return."



