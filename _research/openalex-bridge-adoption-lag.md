---
title: "OpenAlex bridge-work adoption lag pilot"
research_id: "PILOT-RESEARCH-001"
status: "Closed — no primary comparison"
updated: "2026-08-20"
topic: "Research methodology / scholarly metadata"
summary: "A preregistered pilot testing whether a metadata-defined bridge-work group could support an interpretable adoption-lag comparison; the study stopped at a taxonomy-validity gate before the primary outcome comparison."
---

## Research question

Can a reproducible OpenAlex metadata definition of “bridge work” support an interpretable comparison of target-field adoption lag against matched controls?

The pilot used a deliberately narrow operational definition. “Bridge work” here does **not** mean that a paper is scientifically important, genuinely interdisciplinary, or causally responsible for knowledge transfer. It refers only to a classification constructed from the scholarly metadata used in this pilot.

## Method

The study was designed in two stages. The research question, matching logic, quality gates, stop rules, and outcome-comparison conditions were fixed before the primary citation outcome was inspected.

The second, source-exact design constructed matched bridge/control pairs for two publication years and applied a sequence of pre-outcome checks covering index integrity, citation-link integrity, chronology, Crossref checks, group balance, and a blind manual taxonomy audit.

The key taxonomy gate required at least **70%** of non-uncertain audited bridge records to be plausibly classifiable in both Computer Science and Medicine. If that gate failed, the protocol required the study to stop before comparing adoption-lag outcomes.

## Observations and results

The redesigned pipeline produced **1,250 bridge/control pairs in each publication year** and passed the index, citation-link, chronology, Crossref, and balance gates.

The blind taxonomy audit did not pass. Among **38 non-uncertain audited bridge records, 16 (42.1%)** were judged plausibly both Computer Science and Medicine, below the preregistered **70%** minimum.

The protocol therefore stopped at the metadata-quality gate.

**The primary adoption-lag comparison was not run.** No bridge/control effect direction, effect size, significance result, or adoption-lag difference is reported from this pilot.

## Interpretation

The result is a methodological non-result rather than evidence for or against an adoption-lag difference.

The source-exact redesign showed that the mechanical parts of the pipeline could be made reproducible and balanced, but the specific metadata-based bridge classification did not reach the preregistered credibility threshold needed for an interpretable scientific comparison.

The strongest supported conclusion is therefore: **do not use the saved event rows from this pilot as evidence that bridge works are adopted faster, slower, or at the same rate as controls.**

Stopping before the outcome comparison matters because it prevents a weak operational definition from being rescued after the fact by an interesting-looking result.

## Limitations and uncertainty

- The failed gate applies to this operational definition, field pair, audit procedure, and sample. It is not a general evaluation of OpenAlex metadata quality.
- The pilot does not establish whether genuine interdisciplinary work diffuses faster or slower across fields.
- The primary outcome was intentionally left untested after the stop condition was met, so there is no null result to interpret.
- The manual audit was a bounded validity check, not a comprehensive taxonomy study.
- A different bridge definition, field pair, or independently validated classification could produce a feasible design, but that would be a new study rather than a continuation of this result.

## Evidence and artifacts

**Public source:** [OpenAlex](https://openalex.org/) scholarly metadata.

The pilot retained preregistration-style design documents, frozen execution specifications, audit records, and execution results in the internal research archive. They are not linked here because the current public release has been limited to reviewed claims and contains no private operational records.

A later reproducibility release may publish sanitized protocol and result artifacts separately. Until then, this page should be treated as the public claim boundary for the pilot.

## Related work

This was the first bounded original-research pilot in the Studio Lab research line. Its main reusable result is methodological: pre-outcome validity gates can produce a useful research outcome even when the scientific comparison itself is never run.
