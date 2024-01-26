[![DOI](https://zenodo.org/badge/686339559.svg)](https://zenodo.org/doi/10.5281/zenodo.10571416)

## LaTeX Server

This repository contains everything needed to create a small containerised Flask server with a `latexmk` and `texlive` installation.

**Setup**

1. Build an image with `docker build -t latex-service:latest .`

2. Run container and expose a port with `docker run -d -p 32769:5000 --name latex-service latex-service`