# Studio Lab Research

Public research site for selected Studio Lab studies, methods, findings, limitations, and shareable evidence.

## Structure

- `_research/` — published research pages. Each Markdown file becomes a page under `/research/`.
- `research/index.md` — research catalog.
- `templates/research-page.md` — copyable front matter and section structure for new research pages.
- `_layouts/` and `assets/css/` — lightweight Jekyll presentation layer.
- `.github/workflows/pages.yml` — GitHub Pages build and deployment workflow.

## Publishing model

Internal research state and evidence remain in their canonical systems. This repository is a public presentation layer. Public research content should be reviewed before merge rather than copied automatically from internal working material.

A normal update is:

1. create a branch;
2. add or update a Markdown file in `_research/`;
3. open and review a pull request;
4. merge to `main`;
5. GitHub Actions builds and deploys the site.

## One-time GitHub Pages setup

In the repository, open **Settings → Pages → Build and deployment → Source** and choose **GitHub Actions**. The included workflow then deploys pushes to `main`.

Expected project-site URL after Pages is enabled and the first deployment succeeds:

`https://josh-temple.github.io/studio-lab-research/`
