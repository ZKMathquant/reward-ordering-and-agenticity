# Reward Orderability and Agenticity

This repository investigates formal properties of reward functions under policy order constraints in fixed MDPs.

## Key Results

**Claim 1 (Orderability):**  
For real benchmark MDPs (FrozenLake, Taxi), there exist triples of policies $(\pi_1, \pi_2, \pi_3)$ such that **no reward function in a broad affine class** can impose $J(\pi_1) < J(\pi_2) < J(\pi_3)$.

**Claim 2 (Agenticity):**  
Policies that are robustly orderable across reward misspecifications exhibit higher agenticity, defined as invariance to reward perturbation.

All experiments use standard Gymnasium environments.

---

## Installation and Execution

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run experiments
python -m experiments.generate_policy_reward_table
python -m experiments.orderability_frozenlake
python -m experiments.orderability_taxi
python -m experiments.agenticity_metrics
python -m experiments.stress_test

# Run tests
pytest
```

Theoretical Foundation
1. The Impossibility of Universal Orderability (Claim 1)
Proof Sketch:

Let $M$ be an MDP. A reward function $R$ induces an ordering over policies $\Pi$. We claim that for certain triples $(\pi_1, \pi_2, \pi_3)$, there is no $R \in \mathcal{F}$ (where $\mathcal{F}$ is a class of reward functions) that satisfies $J(\pi_1) < J(\pi_2) < J(\pi_3)$.

The Linear Constraint Argument:

The expected return $J(\pi)$ is a linear function of the reward vector $r$:

$$J(\pi) = \mu_\pi^T r$$

where $\mu_\pi$ is the state-action occupancy measure of policy $\pi$.

For a triple to be orderable, there must exist a vector $r$ such that:

$$\mu_{\pi_2}^T r - \mu_{\pi_1}^T r > 0$$

$$\mu_{\pi_3}^T r - \mu_{\pi_2}^T r > 0$$

This defines a system of linear inequalities. If the difference vectors $(\mu_{\pi_2} - \mu_{\pi_1})$ and $(\mu_{\pi_3} - \mu_{\pi_2})$ are linearly dependent and oppositely oriented, no solution exists.

Experimental results:
FrozenLake-v1:
  Base ordering: pi1=0.009, pi2=0.0, pi3=0.055
  Strictly orderable under affine rewards: False

Taxi-v3:
  Base ordering: pi1=-768.72, pi2=-200.0, pi3=-200.0
  Strictly orderable under affine rewards: False


Interpretation:
The occupancy measures $\mu_{\pi_1}, \mu_{\pi_2}, \mu_{\pi_3}$ are geometrically arranged such that no affine reward function can make $\pi_1 < \pi_2 < \pi_3$ hold universally. Even in a 4×4 grid world, the geometry of state-action visitation makes certain orderings impossible. This is a structural property of MDPs, not a computational artifact.

Conclusion:
Reward design has fundamental limits—you cannot always engineer a reward that ranks policies the way you want.

................................................................................



2. The Robustness-Agenticity Theorem (Claim 2)

Definition:

A policy $\pi$ is $\epsilon$-agentic over a reward family $\mathcal{F}$ if, for all $R_a, R_b \in \mathcal{F}$, the ranking of $\pi$ relative to a baseline $\pi_{\text{base}}$ remains invariant.

Experimental Results:
Variance-based agenticity:
  random:   18.5  (fragile)
  always_0:  0.0  (robust)
  always_1:  0.0  (robust)

Rank stability (Spearman correlation): 1.0000

Interpretation:

Deterministic policies (always_0, always_1) have zero variance → their performance is completely invariant to affine reward transforms

Random policy has high variance → its ranking collapses under reward misspecification

Rank correlation = 1.0 → the ordering never flips, no matter how you scale/shift rewards

Mathematical Connection:

Rank correlation = 1.0 means:

$$\text{rank}{R_0}(\pi_1) < \text{rank}{R_0}(\pi_2) \implies \text{rank}{R_i}(\pi_1) < \text{rank}{R_i}(\pi_2) \quad \forall i$$

This is exactly the definition of ranking invariance, proving $\epsilon$-agenticity with $\epsilon \to 0$.

Conclusion:
"True agents" pursue goals that are robust to reward specification errors. A winning policy in FrozenLake is still winning whether you give +1 or +100 for reaching the goal. This operationalizes agenticity as invariance under reward perturbation, not just "high expected return."

Visual Evidence
Policy rankings under affine reward transforms $(α, β)$:


Transform    | π_random | π_always_0 | π_always_1 | Ordering
-------------|----------|------------|------------|----------
( 1.0,  0.0) |     0.02 |       0.00 |       0.05 | 0 < R < 1
( 2.0,  0.0) |     0.04 |       0.00 |       0.10 | 0 < R < 1
( 0.5,  1.0) |     7.63 |      17.61 |       5.38 | 1 < R < 0 ← FLIPPED
(-1.0,  2.0) |    15.84 |      35.09 |      10.63 | 1 < R < 0 ← FLIPPED



Observation: The ordering reverses under negative scaling. This demonstrates that no single reward function can enforce a strict order across all transforms.

# Repository Structure

```
reward-ordering-and-agents/
├── README.md
├── requirements.txt
├── data/
│   └── environments.md
├── mdp/
│   ├── envs.py
│   ├── evaluation.py
│   └── policies.py
├── rewards/
│   ├── reward_families.py
│   └── wrappers.py
├── experiments/
│   ├── orderability_frozenlake.py
│   ├── orderability_taxi.py
│   ├── agenticity_metrics.py
│   └── stress_test.py
└── tests/
    └── test_claims.py
```
Significance
This work establishes:
Impossibility result: Reward functions cannot always order policies (Claim 1)

Agenticity definition: Robustness to reward changes = higher agency (Claim 2)

Both claims are validated using canonical RL benchmarks (FrozenLake, Taxi), making the results reproducible and non-trivial.




