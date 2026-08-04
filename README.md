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

**"What is a Qubit?" — a browser-based quantum starter kit that runs without installation.**

Built with **Quarto × marimo**, this kit uses coin analogies and **live circuit
simulations** so that even middle school students can intuitively grasp the core
concepts of quantum computing — superposition, entanglement, and quantum
algorithms.

- **Everything runs in the browser** (WebAssembly / Pyodide). No installation needed.
- **Interactive demos** — move a slider or click a gate, and the probability and histogram update instantly.
- **Qiskit notebooks** included for those ready to try a real quantum SDK.

## Motivation

Quantum computing sounds fascinating, but most tutorials assume you already know
linear algebra and Dirac notation. Inspired by *Nielsen & Chuang*, I wanted a
place where learners can *feel* superposition and entanglement before ever
writing a formula — by touching sliders and watching a coin toss turn into a
quantum coin.

This kit started as a draft produced through a long, long conversation with an
OpenAI LLM. There is still a lot for us to learn about quantum computing, so the
content is by no means authoritative — feedback and corrections are very welcome.

## Features

- **Runs in the browser** — demos execute on Pyodide (WASM); zero setup
- **Six interactive lessons** — Qubit, superposition, entanglement, gates, measurement, algorithms
- **Live simulations** — state vectors and histograms recalculate in real time
- **Printable worksheets** — for classroom use and self-study review
- **Qiskit notebooks** — hands-on experiments with the real quantum SDK (local run)
- **Self-contained numpy simulator** — an educational state-vector simulator (`lib/sim.py`)
- **Auto-deployed** — GitHub Pages workflow publishes the latest site on every push

## Screenshot

<!-- Add screenshots here -->

Try the live site: [Quantum Computer Starter Kit](https://watanabe3tipapa.github.io/ir-qubit/)

## Installation

```bash
# 1) Environment setup (with uv)
uv sync

# or, with a plain venv
python -m venv .venv
source .venv/bin/activate
pip install marimo numpy matplotlib qiskit qiskit-aer
```

## Usage

```bash
# Local preview at http://localhost:4321
uv run quarto preview

# Build the static site into _site/
uv run quarto render
```

Run the Qiskit notebooks on your own machine:

```bash
uv run marimo edit notebooks/01_qubit_superposition.py
uv run marimo edit notebooks/02_entanglement.py
```

> Technical note: the in-page demos run on Pyodide (WASM), so they rely only on
> numpy / matplotlib. Qiskit is Rust-based and cannot run in WASM, so the site
> ships its own educational numpy simulator and bundles Qiskit notebooks for
> local execution. See [DEV-MEMO.md](DEV-MEMO.md) for details.

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a [Pull Request](https://github.com/watanabe3tipapa/ir-qubit/pulls)

## License

- **Documentation & images**: [CC BY 4.0](LICENSE-CC-BY)
- **Code**: [Apache-2.0](LICENSE)

## Contact

GitHub: [https://github.com/watanabe3tipapa/ir-qubit](https://github.com/watanabe3tipapa/ir-qubit)
