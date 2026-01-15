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

