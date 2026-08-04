import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # 02｜エンタングルメント（Qiskit 版）

    Qiskit でベル状態（エンタングルメント）を作って測定します。
    """
    )
    return


@app.cell
def _(mo):
    shots = mo.ui.slider(100, 8192, value=1024, step=32, label="測定回数（shots）")
    shots
    return (shots,)


@app.cell
def _(mo, shots):
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    import matplotlib.pyplot as plt

    plt.rcParams["font.family"] = [
        "Hiragino Sans",
        "Arial Unicode MS",
        "Yu Gothic",
        "sans-serif",
    ]
    plt.rcParams["axes.unicode_minus"] = False

    # 2 qubit：H のあと CNOT → ベル状態
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    result = AerSimulator().run(qc, shots=shots.value).result()
    counts = result.get_counts()

    fig, ax = plt.subplots(figsize=(6, 3.6))
    keys = sorted(counts.keys())
    ax.bar(keys, [counts[k] for k in keys], color="#f58518")
    ax.set_title(f"ベル状態の測定結果（{shots.value} shots）")
    ax.set_xlabel("測定結果（qubit0 qubit1）")
    ax.set_ylabel("回数")
    plt.close(fig)

    mo.hstack(
        [mo.mpl.interactive(fig), mo.md(f"**counts**: {counts}")], justify="start"
    )
    return AerSimulator, QuantumCircuit, counts, fig, plt, qc, result


@app.cell
def _(mo):
    mo.md(
        r"""
    **観察ポイント**

    - 出力は `00` と `11` が圧倒的に多く、`01` や `10` はほとんど出ない。
    - 2 つのビットは常に **同じ** 向き（エンタングルメント！）。
    """
    )
    return


if __name__ == "__main__":
    app.run()
