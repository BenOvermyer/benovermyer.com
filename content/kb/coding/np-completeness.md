+++
title = "NP Completeness"
description = "My notes on what NP and related concepts are"

[extra]
render_math = true
+++

## Terminology

**P:** Polynomial time. Problems that can be solved "efficiently." Here, efficiently means in polynomial time.

**NP:** Non-deterministic polynomial time. Problems for which a candidate solution can be *verified* efficiently.

**NP-hard:** A problem is NP-hard if every problem in NP can be reduced to that problem in polynomial time.

**NP-complete:** A problem is NP-complete if it is both in NP and it is NP-hard.

NP-complete problems are the hardest problems in NP. If you can solve one efficiently, you can solve all NP problems efficiently.

## Proving NP-completeness

To prove a problem is NP-complete, you have to do two things: show it is in NP, and show it is NP-hard.

Showing $X \in NP$:

* Find a way to verify a candidate solution in polynomial time
* Example: for SubsetSum, if someone gives you a subset of numbers, you can quickly sum them and check if it equals the target.

Showing $X$ is NP-hard:

* Take a known NP-complete problem $Y$ and show that it can be reduced to $X$ in polynomial time
* Given that "reduction" means that solving $X$ would also solve $Y$, this proves that $X$ is at least as hard as $Y$

## Polynomial-time reduction

If you have a known NP-complete problem $Y$, you construct a function $f$ that maps instances of $Y$ to instances of $X$ efficiently.

$f$ must preserve the answer:

* $Y$ instance is "yes" $\implies X$ instance is "yes"
* $Y$ instance is "no" $\implies X$ instance is "no"

If this works, solving $X$ solves $Y$, so $X$ is at least as hard as $Y$.

## Use a known NP-complete problem

Some common NP-complete problems that you can use as starting points:

* SAT (boolean satisfiability problem)
* 3-SAT (a specific version of SAT)
* Clique
* Vertex-Cover
* SubsetSum

## Summation

1. Show $X \in NP$
2. Choose a known NP-complete problem $Y$
3. Construct a polynomial-time reduction from $Y$ to $X$
  * Show that every instance of $Y$ can be transformed into an instance of $X$ in polynomial time
  * Verify that the answers correspond
4. Conclude: $X$ is NP-complete

## Example: Proving Double SAT is NP-Complete

First, what is Double SAT?

Input: A boolean formula $\phi$ in CNF (conjunctive normal form).

Question: Are there at least two distinct satisfying assignments for $\phi$?

### Step One: Show Double SAT $\in$ NP

To show this is in NP, we must show that a candidate solution can be verified in polynomial time.

Candidate solution: two assignments $A_1$ and $A_2$.

Verification algorithm:

1. Check that $A_1$ satisfies $\phi$
2. Check that $A_2$ satisfies $\phi$
3. Check that $A_1 \neq A_2$

Each check is polynomial time, because evaluating a CNF formula is linear in the size of the formula, and comparing two assignments is linear in the number of variables.

Therefore, Double SAT $\in$ NP.

### Step Two: Show Double SAT is NP-hard

We do this by reducing a known NP-complete problem to Double SAT. We'll use 3-SAT as the known NP-complete problem.

Given a 3-SAT formula $\phi$, we want to create a formula $\phi\prime$ such that:

* $\phi$ is satisfiable $\implies \phi\prime$ has at least two satisfying assignments
* $\phi$ is unsatisfiable $\implies \phi\prime$ has zero satisfying assignments

If we can do this, then solving Double SAT on $\phi\prime$ tells us whether $\phi$ is satisfiable.

1. Let $\phi$ be a 3-SAT formula over variables $x_1, x_2,...,x_n$
2. Introduce a new variable $y$
3. Define $\phi\prime = \phi \land (y \lor \neg y)$

Explanation of the formula from 3:

* The clause $(y \lor \neg y)$ is always true
* Therefore, $\phi\prime$ is satisfiable if and only if $\phi$ is satisfiable
* But now, for every satisfying assignment of $\phi$, there are two ways to assign $y$: true or false
* So, if $\phi$ has at least one satisfying assignment, $\phi\prime$ automatically has at least two distinct satisfying assignments

Case 1: $\phi$ is unsatisfiable

In this case, $\phi\prime$ is also unsatisfiable $\implies$ zero satisfying assignments.

Case 2: $\phi$ is satisfiable

If $\phi$ has a satisfying assignment $A$, then $\phi\prime$ can be satisfied by $A \cup { y = True }$ and $A \cup { y = False } \implies$ two distinct satisfying assignments.

Thus, $\phi$ is satisfiable $\implies \phi\prime$ has $\geq 2$ solutions, and $\phi$ is unsatisfiable $\implies \phi\prime$ has 0 solutions.

### Step Three: Polynomial-Time Reduction

From step two, we can see that adding a new variable and a single tautology clause is clearly polynomial in time and size.

### Step Four: Conclude NP-Completeness

Since we have shown that Double SAT $\in$ NP and 3-SAT $\leq_p$ Double SAT, Double SAT is NP-complete.
