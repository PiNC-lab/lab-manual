# PiNC Lab Manual

Tutorials, how-to guides and shared resources for the [People in Nature & Climate (PiNC) Lab](https://www.pinclab.co.za) at the University of Cape Town.

**The site is at <https://pinc-lab.github.io>.**

## Contributing

Anyone in the lab can fix a page or add a new tutorial, and you can do it all in your web browser. The short version:

1. **Fork** this repository (the **Fork** button at the top right of this page). This makes your own copy.
2. **Edit or add files** in your fork. Tutorials go in the `tutorials` folder as `.qmd` files. Start from [`tutorials/_template.qmd`](tutorials/_template.qmd).
3. **Open a pull request** to ask for your change to be added to the lab's copy. Someone will review it and merge it.

For small fixes it's even simpler: click **Edit this page** on any page of the website, and GitHub sets up the fork and pull request for you.

The [Contributing page](https://pinc-lab.github.io/contributing.html) has click-by-click instructions, plus Markdown basics and how to add images.

## What's in this repository

| File or folder | What it is |
|---|---|
| `index.qmd` | The home page |
| `tutorials/` | One `.qmd` file per tutorial or how-to. Images go in `tutorials/images/` |
| `tutorials/_template.qmd` | A starting point for new tutorials (not shown on the site) |
| `resources.qmd` | Useful links |
| `contributing.qmd` | How to contribute |
| `_quarto.yml` | Site settings and the menu bar. You won't usually need to change this |
| `.github/workflows/publish.yml` | Builds and publishes the site automatically |

The site is built with [Quarto](https://quarto.org). Every change merged into `main` is published automatically by GitHub Actions. Pull requests are checked to make sure the site still builds.

To preview the whole site on your own computer, install Quarto (it comes with RStudio) and run `quarto preview` in this folder.
