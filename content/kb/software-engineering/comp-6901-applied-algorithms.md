+++
title = "COMP 6901: Applied Algorithms"

[extra]
render_math = true
+++

The following are my notes for my applied algorithms course. They're not in any particular order.

## Big O Notation

$ O(1) $ is **constant time**. The running time is not dependent on the size of the input.

$ O(n) $ is **linear time**. The running time grows linearly with the size of the input.

$ O(\log n) $ is **logarithmic time**. The running time depends on half the input size. Binary search algorithms are $\log n$.

$ O(n^2) $ is **quadratic time**. The running time grows to the power of two with the size of the input. This is bad. Think nested loops.

$ O(2^n) $ is **exponential time**. The running time doubles each time the input increases.

## Other Details

When evaluating algorithms with big O notation, you can ignore the base of a logarithm.

Exponentials are always different.

$$ a^{2n} \notin O(a^n) $$

Factorials are roughly equivalent to $ n^n $ in terms of Big O. Stirling's formula is given as a proof of this.

$$ n! \approx \sqrt{2\pi n}\left(\frac{n}{e}\right)^n $$

P is polynomial time to find a solution, and NP is polynomial time to check a solution.

## Stable Matching

Given a set of hospitals M and a set of students N, find a set of matches between hospitals and students where each pairing is stable, assuming that each has a set of three preferences in descending order.

With the above scenario as context, a stable match is when neither side of a pairing has another possible pairing which would be preferred by both sides of the pairing.

## Gale-Shapley

Gale-Shapley is an algorithm that implements stable matching. It goes as follows:

- in each round, one or more hospitals without a match selects a student that they prefer.
- each student that receives an offer compares it to their current match, if they have one. If they don't yet have one, or they receive an offer from a hospital they prefer more than their current match, then they accept the offer. Otherwise, they reject the offer.
- repeat until all hospitals have a match or until no students are available.

## Graphs

## Topological Sort

## Greedy Algorithms

Greedy algorithms take the best option at each iteration, rather than the best option given full context of the problem and the current state.
