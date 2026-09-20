---
layout: research
title: "Heckerman et al. (2025): a bounded check of the reported fully-replicable proportion"
research_id: "PILOT-RESEARCH-001 / Heckerman 2025 bounded numeric replication"
status: "Completed — bounded calculation reproduced"
updated: "2026-09-20"
topic: "Research methodology / reproducibility"
summary: "A pre-specified arithmetic check reproduced 5 / 393 = 1.27% from Heckerman et al. (2025). This verifies one reported numeric relation, not a general replicability rate or the paper's broader conclusions."
---

## Current conclusion

A bounded replication of one reported numeric relation **passed**.

Heckerman et al. (2025) report **393 empirical research studies** in the assessed set and **5 studies** in their `fully replicable` category. Studio Lab fixed the calculation in advance as:

**5 / 393 × 100**

with no intermediate rounding and a final result rounded to two decimal places.

The recomputed value is **1.27%**.

## What was checked

This was deliberately a small test. The inputs were fixed to the two source counts:

- empirical research studies: **393**
- studies classified as fully replicable: **5**

The only calculation was the proportion represented by those counts. No alternative denominator, category, threshold, or subgroup was introduced after the result.

Under that bounded specification, the source paper's statement that the fully-replicable share was **below 2%** is numerically consistent with the reported counts.

## What this does not reproduce

This page does **not** independently re-review the 393 empirical studies.

It therefore does not establish that:

- 1.27% is the replicability rate of all cardiovascular research;
- the same proportion applies to medicine or science generally;
- every underlying paper was classified correctly;
- the paper's full methodology or conclusions have been independently replicated.

The verified claim is narrower: **given the paper's reported counts of 5 and 393, the pre-specified percentage is 1.27%.**

## Why publish such a small replication?

Percentages can look more general than the counts and definitions underneath them. A bounded recomputation makes the denominator, numerator, rounding rule, and claim ceiling explicit before interpretation expands.

This is useful even when the arithmetic is simple: it records exactly what was reproduced and, just as importantly, what was not.

## Source

Primary source: Heckerman GO, Tzng E, Campos-Melendez A, et al. *Transparency of research practices in cardiovascular literature*. eLife. 2025;14:e81051.

- https://elifesciences.org/articles/81051
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12068865/

## Evidence boundary

This is a bounded numeric replication of one relation reported in a published paper. It is not a clinical conclusion, a medical recommendation, or an estimate of reproducibility across other populations of research.
