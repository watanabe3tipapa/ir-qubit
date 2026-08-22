<!-- badges -->
[![License](https://img.shields.io/github/license/watanabe3tipapa/ir-qubit.svg)](LICENSE)
[![Quarto](https://img.shields.io/badge/Quarto-1.9-1496cc?logo=quarto&logoColor=white)](https://quarto.org)
[![marimo](https://img.shields.io/badge/marimo-0.23+-6E4B9C)](https://marimo.io)
[![Python](https://img.shields.io/badge/Python-3.12%7C3.13-3776AB?logo=python&logoColor=white)](https://python.org)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-brightgreen.svg)](https://github.com/watanabe3tipapa/ir-qubit)
[![Last commit](https://img.shields.io/github/last-commit/watanabe3tipapa/ir-qubit/main.svg)](https://github.com/watanabe3tipapa/ir-qubit/commits/main)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-2ea44f)](https://watanabe3tipapa.github.io/ir-qubit/)

[English](README.md) | [日本語](README_ja.md)

# Quantum Computer Starter Kit

"What is a Qubit?" — a browser-based quantum starter kit that runs without
installation.

This project is an educational set of interactive lessons and demonstrations
that aim to make core quantum computing ideas—superposition, entanglement, and
basic quantum algorithms—accessible through hands-on, browser-executed demos.
The site is built with Quarto and marimo and includes both in-page WebAssembly
(Pyodide) simulations and offline Qiskit notebooks for local experimentation.

Live demo: https://watanabe3tipapa.github.io/ir-qubit/

## What this repository contains

- Six interactive lessons (concepts include qubit, superposition,
  entanglement, gates, measurement, and algorithms)
- Browser-executed demos implemented to run on Pyodide (WASM) so they work in
  the browser without installing Python packages
- A self-contained educational state-vector simulator: lib/sim.py
- Qiskit notebooks for local execution (not runnable in the browser)
- Printable worksheets for classroom or self-study use
- Quarto site sources and a GitHub Pages deployment (the site is auto-deployed)

## Key features

- Runs in the browser via Pyodide (no installation required for the in-page demos)
- Interactive controls: sliders and clickable gates update state vectors and
  histograms in real time
- Qiskit notebooks included for users who want to run experiments locally
- Educational numpy-based simulator included for WASM-executed demos

## Motivation

Many introductions to quantum computing assume prior knowledge of linear
algebra and Dirac notation. This starter kit emphasizes intuition-through
interaction: learners can manipulate parameters and immediately observe the
probabilistic outcomes and state changes.

The project began as a draft and continues to be improved; feedback and
corrections are welcome.

## Try it locally

The repository includes development tooling and commands in the top-level
README. Example steps that appear in the project sources:

Installation (examples shown in the project README):

```bash
# Option A: sync with uv (project uses 'uv' in examples)
uv sync

# Option B: plain virtual environment
python -m venv .venv
source .venv/bin/activate
pip install marimo numpy matplotlib qiskit qiskit-aer
```

Preview and build (examples shown in the project README):

```bash
# Local preview at http://localhost:4321
uv run quarto preview

# Build the static site into _site/
uv run quarto render
```

Qiskit notebooks (run locally):

```bash
uv run marimo edit notebooks/01_qubit_superposition.py
uv run marimo edit notebooks/02_entanglement.py
```

Notes and technical details are available in DEV-MEMO.md in the repository.

## Development and dependencies

The project metadata (pyproject.toml) declares:

- requires-python = ">=3.13"
- dependencies include: altair, marimo, matplotlib, numpy, pandas, qiskit,
  qiskit-aer (specific versions are listed in pyproject.toml)

Refer to pyproject.toml and the repository files for exact dependency versions
and development instructions.

## Contributing

Contributions are welcome. The repository's README lists a standard GitHub
workflow for contributions:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a Pull Request

Please follow existing project conventions and open issues or PRs on GitHub.

## License

- Documentation & images: CC BY 4.0 (see LICENSE-CC-BY)
- Code: Apache-2.0 (see LICENSE)

## Project status

- Repository updated at: 2026-08-08T22:09:55Z
- The project is not archived and has an active maintenance badge in the
  repository README.

## Contact

GitHub: https://github.com/watanabe3tipapa/ir-qubit
Website (live demo): https://watanabe3tipapa.github.io/ir-qubit/
