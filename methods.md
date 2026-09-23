---
title: Methods
permalink: /methods/
description: Public research and publishing methods used by Studio Lab.
---

<p class="eyebrow">Methods</p>
<h1>Make the stopping rules visible.</h1>
<p class="lede">Studio Lab treats a study as useful even when the correct outcome is to stop before the headline result. The public method is built around claim boundaries, observable checks, and explicit uncertainty.</p>

<div class="prose">
## Separate observation from interpretation

A research page distinguishes what was directly observed from what the observations may support. A measurement, audit result, failed validity check, or completed execution is not automatically a broader scientific conclusion.

## Fix important gates before looking at the result

When a validity condition can determine whether a comparison is interpretable, the condition should be specified before the primary outcome is inspected. The OpenAlex pilot is the first published example: its taxonomy-validity gate failed, so the adoption-lag comparison was not run.

## Treat stopping as a result

Stopping is not the same as finding no effect. If a study ends before its primary comparison, the public record should say that the outcome is unobserved rather than silently converting the stop into a null result.

## Keep data-availability failures separate from hypothesis results

If the value that would have been available at a historical decision time cannot be reconstructed reliably, a retrospective test should remain unobserved or move to a prospective design. Revised history, a convenient substitute series, or a later snapshot should not be used to manufacture a result that the original information boundary cannot support.

## Verify the retrieval path, not only the source name

An official page can establish that a dataset or instrument exists without proving that the assigned execution environment can retrieve the required historical observations reproducibly. Before a result-bearing test, Studio Lab separately checks the machine-readable representation, exact instrument or field identity, request shape, authentication or entitlement requirements, and any observation-time persistence requirement. If one required input path remains unresolved, the test stays on hold rather than substituting a convenient provider, series, contract, or later-revised value.

A failed retrieval path is treated as local evidence about that path, not as proof that the scientific hypothesis failed or that the entire provider is unavailable. The same unresolved representation is not silently reused until there is evidence that the access condition changed.

Recent three-case review added a provisional constraint to this preflight logic: the preflight itself must respect the study's information boundary. If outcome blinding forbids reading target values and a safe non-target probe cannot be constructed, the path remains **unverified / HOLD** rather than being labeled unavailable. A probe that breaks the frozen outcome boundary is not valid evidence of retrievability. This boundary remains provisional rather than a generalized rule about providers.

## Do not let automation fill unresolved scientific conditions

A candidate can remain scientifically interesting without being ready to test. If an evaluation window, threshold, baseline, feed, cost rule, or candidate choice still has no unique pre-outcome rule, automation stops at a human boundary rather than inventing a convenient default. The choice must be fixed before unused or prospective outcomes are opened; if there is no safe default, the correct state is HOLD.

## Keep claims inside the measured scope

A proxy should remain a proxy. A metadata classification does not become a direct measure of scientific value, organizational maturity, adoption, or causality simply because it is convenient to compute.

## Preserve an audit trail without publishing everything

The public site records the method, claim boundary, result category, and appropriate public evidence. Internal working documents, private data, credentials, operational logs, and unreleased artifacts stay outside the public layer unless there is a specific reason to publish them.

## Use human review at the publication boundary

Automation can prepare pages and checks, but substantive public claims are reviewed before they are merged into the publishing branch. The goal is not to automate publication at any cost; it is to reduce the work required to publish carefully.
</div>

<section class="section public-boundary">
  <p class="eyebrow">Example</p>
  <h2>OpenAlex bridge-work adoption-lag pilot</h2>
  <p>The first published study demonstrates the method in practice: a preregistered validity gate failed before the primary comparison, and the page reports that boundary rather than an effect estimate.</p>
  <a href="{{ '/research/openalex-bridge-adoption-lag/' | relative_url }}">Read the study</a>
</section>
