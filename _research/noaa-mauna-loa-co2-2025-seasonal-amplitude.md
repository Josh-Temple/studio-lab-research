---
layout: research
title: "Mauna Loa CO₂ in 2025: a bounded monthly seasonal-amplitude check"
research_id: "PILOT-RESEARCH-001 / NOAA GML Mauna Loa CO2 2025 seasonal amplitude"
status: "Completed — bounded threshold test passed"
updated: "2026-09-25"
topic: "Public data / bounded empirical test"
summary: "Using NOAA GML's 12 monthly-average CO₂ values for Mauna Loa in 2025, a pre-specified max-minus-min calculation produced 6.14 ppm, above the fixed 5 ppm threshold. The result is descriptive and limited to one site and one year."
---

## Current conclusion

The bounded test **passed its pre-specified threshold**.

Studio Lab used NOAA Global Monitoring Laboratory's monthly mean CO₂ series for Mauna Loa and fixed the calculation to the maximum minus the minimum of the 12 monthly-average values for **2025**.

The result was:

- maximum monthly average: **430.51 ppm** in May;
- minimum monthly average: **424.37 ppm** in September;
- max minus min: **6.14 ppm**;
- fixed threshold: **5 ppm**.

Under that specification, **6.14 ppm > 5 ppm**, so the bounded test result is **PASS**.

## Source preflight

The data path was checked before the target-year values were used.

The source was fixed to NOAA GML's official plain-text Mauna Loa monthly mean file:

https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt

The field was fixed to the file's **monthly average** column. The de-seasonalized column was not substituted, and the 2025 result was not calculated until the text representation and field identity had been verified as readable in the execution path.

This matters because several other public-data candidates in the same research program stopped before outcome retrieval when their exact machine-readable representation could not be verified.

## Monthly values used

| Month | Monthly average CO₂ |
|---|---:|
| Jan | 426.65 ppm |
| Feb | 427.09 ppm |
| Mar | 428.15 ppm |
| Apr | 429.64 ppm |
| May | 430.51 ppm |
| Jun | 429.61 ppm |
| Jul | 427.87 ppm |
| Aug | 425.48 ppm |
| Sep | 424.37 ppm |
| Oct | 424.87 ppm |
| Nov | 426.46 ppm |
| Dec | 427.49 ppm |

The calculation uses all 12 monthly values and no alternative month selection.

## What this result shows

For **Mauna Loa in calendar year 2025**, the difference between the highest and lowest NOAA GML monthly-average CO₂ values was **6.14 ppm**, which exceeded the fixed 5 ppm threshold used in this test.

That is the full claim.

## What this result does not show

This test does not establish:

- the cause of the within-year pattern;
- a global CO₂ seasonal amplitude;
- the amplitude in other years or at other monitoring sites;
- a long-term trend estimate;
- a climate attribution claim.

The result is a bounded descriptive calculation from one official station series over one calendar year.

## Why this test matters for the research process

The substantive calculation is simple. The more important methodological point is that **retrieval readiness and the empirical result were kept separate**.

When an exact source path and field identity could not be verified for other candidates, those studies stayed on hold rather than switching to a convenient substitute. Here, the official text representation was reproducibly readable, so the test could proceed without changing the frozen data definition.

## Decision implication

This result is sufficient to close this bounded one-year threshold test: no rescue tuning or additional month selection is needed. It should not be promoted into a claim about other years, other stations, global seasonal amplitude, or causality. A broader question should be framed as a separate study with its own pre-outcome scope and data definition.

## Source

Primary source: NOAA Global Monitoring Laboratory, *Trends in Atmospheric Carbon Dioxide — Mauna Loa monthly mean CO₂*.

- https://gml.noaa.gov/ccgg/trends/
- https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt

## Evidence boundary

This page reports a pre-specified arithmetic comparison using NOAA GML's published monthly-average values. It should be read as a one-site, one-year descriptive result, not as a broader causal or climatological conclusion.
