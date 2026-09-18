# Studio Lab

Public Studio Lab hub for selected research, projects, writing, and methods.

The repository name remains `studio-lab-research`, but the GitHub Pages site serves as the outward-facing Studio Lab dashboard. Internal operational state belongs in the private dashboard; this repository contains reviewed public outputs and links.

## Structure

- `_research/` — published research pages. Each Markdown file becomes a page under `/research/`.
- `research/index.md` — research catalog and research-area entry points.
- `trading.md` — public landing page for reviewed systematic-trading research.
- `market.md` / `ja/market.md` — lightweight public market-observation pages built from an hourly snapshot; descriptive data only, separate from trading decisions and internal telemetry.
- `projects.md` — selected public projects and links to the curated Baukasten portfolio.
- `writing.md` — curated links to published writing.
- `methods.md` — public research and publication principles.
- `about.md` — boundary between the internal dashboard and public site.
- `templates/research-page.md` — copyable structure for new research pages, including optional visualization guidance.
- `_layouts/` and `assets/css/` — lightweight Jekyll presentation layer, including reusable no-JavaScript metric-chart styles.
- `.github/workflows/pages.yml` — GitHub Pages build and deployment workflow.

## Publishing model

Internal research state, live work queues, private data, credentials, operational logs, drafts, unpublished claims, positions, and current trade decisions remain in their canonical systems. This repository is a public presentation layer. The `/market/` page is a narrow exception for public descriptive observations: it publishes only a bounded market snapshot and standard indicators, not Studio Lab control state or trading instructions.

A normal substantive update is:

1. create a branch;
2. add or update the relevant public page;
3. open and review a pull request;
4. merge to `main`;
5. GitHub Actions builds and deploys the site.

Trading research follows the same boundary: reviewed historical or simulated findings may be published, while live positions, account information, current trade decisions, and unresolved experiments remain private.

The public market page refreshes hourly through the Pages build and fails closed when the market-data source is unavailable.

## Public site

https://josh-temple.github.io/studio-lab-research/

## Related public portfolio

Baukasten is the curated source of truth for project selection and verified project links:

https://josh-temple.github.io/Baukasten/
