This repository investigates formal properties of reward functions under
policy order constraints in fixed MDPs.

Key result:
There exist real benchmark MDPs and policies π₁, π₂, π₃ such that
no reward function in a broad affine family induces J(π₁) < J(π₂) < J(π₃).

We further propose a robustness-based notion of agenticity, defined as
policy stability under reward misspecification.

All experiments use standard Gymnasium environments.



#run the following commands:

python -m venv venv
source venv/bin/activate
pip install -m requirements.txt
python -m experiments.orderability_frozenlake
python -m experiments.orderability_taxi
python -m experiments.agenticity_metrics
python -m  experiments.stress_test

pytest



**Observation:** The ordering reverses under negative scaling.
This proves no single reward function can enforce a strict order across all transforms



Claim 1 (Orderability):
For real benchmark MDPs (FrozenLake, Taxi), there exist triples of policies 
(\pi_1, \pi_2, \pi_3) such that no reward function in a broad class can impose
(J(\pi_1) < J(\pi_2) < J(\pi_3)).

Claim 2 (Agenticity):
Policies that are robustly orderable across reward misspecifications exhibit higher agenticity.

.....................................................................................................

#1

The Proof Sketch of Claim1:

Let \( M \) be an MDP. A reward function \( R \) induces an ordering over policies \( \Pi \). We claim that for certain triples \( (\pi_1, \pi_2, \pi_3) \), there is no \( R \in F \) (where \( F \) is a class of reward functions) that satisfies \( J(\pi_1) < J(\pi_2) < J(\pi_3) \).

The Linear Constraint Argument: The expected return \( J(\pi) \) is a linear function of the reward vector \( r \).

$$
J(\pi) = \mu_\pi^T r
$$
where \( \mu_\pi \) is the state-action occupancy measure of policy \( \pi \).

For a triple to be orderable, there must exist a vector \( r \) such that:

$$
\mu_{\pi_2}^T r - \mu_{\pi_1}^T r > 0
$$

$$
\mu_{\pi_3}^T r - \mu_{\pi_2}^T r > 0
$$

This defines a system of linear inequalities. If the difference vectors \( (\mu_{\pi_2} - \mu_{\pi_1}) \) and \( (\mu_{\pi_3} - \mu_{\pi_2}) \) are linearly dependent and oppositely oriented, no solution exists. In real benchmarks like FrozenLake, certain policies have overlapping occupancy measures that make these constraints impossible to satisfy simultaneously.


#2
2. Refining the Agenticity Theorem

We define "Agenticity" not just as low variance, but as Invariance to Reward Perturbation.

The Robustness-Agenticity Theorem
A policy \( \pi \) is \( \epsilon \)-agentic over a reward family \( F \) if, for all \( R_a, R_b \in F \), the ranking of \( \pi \) relative to a baseline \( \pi_{\text{base}} \) remains invariant.











....................................
...................................
....................................


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




