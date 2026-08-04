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
    # 01｜Qubit の重ね合わせ（Qiskit 版）

    ブラウザのデモは numpy で作った簡易シミュレータでしたが、こちらは本物の量子 SDK
    **Qiskit** を使ったバージョンです。自分の PC で実行できます。
    """
    )
    return


@app.cell
def _(mo):
    shots = mo.ui.slider(10, 8192, value=1024, step=10, label="測定回数（shots）")
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

    # 1 qubit の回路：アダマールゲートで重ね合わせ
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    # シミュレータで実行
    result = AerSimulator().run(qc, shots=shots.value).result()
    counts = result.get_counts()

    fig, ax = plt.subplots(figsize=(6, 3.6))
    keys = sorted(counts.keys())
    ax.bar(keys, [counts[k] for k in keys], color="#4c78a8")
    ax.set_title(f"H ゲートの測定結果（{shots.value} shots）")
    ax.set_xlabel("測定結果")
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

    - `0` と `1` がほぼ同じ回数出る（50%:50%）。
    - スライダーで測定回数を増やすと、分布がきれいに半々に収束する。
    """
    )
    return


if __name__ == "__main__":
    app.run()
