+++
title = "Boolean Algebra"
description = "Notes about boolean algebra"

[extra]
render_math = true
+++

# Annulment Law

A term "AND"-ed with 0 is always 0.

A term "OR"-ed with 1 is always 1.

# De Morgan's Laws

1. The negation of a disjunction is the conjunction of the negations
2. The negation of a conjunction is the disjunction of the negations

or

1. The complement of a union of two sets is the same as the intersection of their complements
2. The complement of an intersection of two sets is the same as the union of their complements

or

1. not (A or B) = not A and not B
2. not (A and B) = not A or not B

Formally written, these are:

$$ \\neg(P \\vee Q) \\Leftrightarrow (\\neg P) \\wedge (\\neg Q) $$

and

$$ \\neg(P \\wedge Q) \\Leftrightarrow (\\neg P) \\vee (\\neg Q) $$

# Identity Law

A term "OR"-ed with 0 or "AND"-ed with 1 will always equal that term.
