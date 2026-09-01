# Studio Lab

Public Studio Lab hub for selected research, projects, writing, and methods.

The repository name remains `studio-lab-research`, but the GitHub Pages site now serves as the outward-facing Studio Lab dashboard. Internal operational state belongs in the private dashboard; this repository contains reviewed public outputs and links.

## Structure

- `_research/` — published research pages. Each Markdown file becomes a page under `/research/`.
- `research/index.md` — research catalog.
- `projects.md` — selected public projects and links to the curated Baukasten portfolio.
- `writing.md` — curated links to published writing.
- `methods.md` — public research and publication principles.
- `about.md` — boundary between the internal dashboard and public site.
- `templates/research-page.md` — copyable structure for new research pages.
- `_layouts/` and `assets/css/` — lightweight Jekyll presentation layer.
- `.github/workflows/pages.yml` — GitHub Pages build and deployment workflow.

## Publishing model

Internal research state, live work queues, private data, credentials, operational logs, drafts, and unpublished claims remain in their canonical systems. This repository is a public presentation layer.

A normal substantive update is:

1. create a branch;
2. add or update the relevant public page;
3. open and review a pull request;
4. merge to `main`;
5. GitHub Actions builds and deploys the site.

## Public site

https://josh-temple.github.io/studio-lab-research/

## Related public portfolio

Baukasten is the curated source of truth for project selection and verified project links:

https://josh-temple.github.io/Baukasten/
