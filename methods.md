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
