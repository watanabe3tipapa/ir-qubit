# 量子コンピュータ入門キット

**「Qubitって何？」から始める、ブラウザで動く量子入門教材（Quarto × marimo）**

中学生でも量子コンピュータの基本概念を直感的につかめるよう、
コインの例えと **動く回路シミュレーション**（marimo islands）を組み合わせた Web サイトです。

- サイト内のデモは **ブラウザ上（WebAssembly / Pyodide）** で動きます。インストール不要。
- 本格的な量子 SDK **Qiskit** を使った marimo ノートブックも同梱しています。

## 構成

```
ir-qubit/
├── _quarto.yml               # Quarto サイト設定（+ marimo 用 pyproject）
├── index.qmd                 # LP（ランディングページ）
├── lessons/                  # レッスン6本（インタラクティブ・デモ入り）
├── worksheets.qmd            # ワークシート（印刷用）
├── notebooks.qmd             # Qiskit ノートブックの使い方
├── notebooks/                # ローカル実行用 marimo（Qiskit 版）
│   ├── 01_qubit_superposition.py
│   └── 02_entanglement.py
├── lib/sim.py                # 教育用 numpy シミュレータ（リファレンス）
├── lib/sim_cell.qmd          # 同上（レッスンの背景セルに include）
└── _extensions/marimo-team/  # quarto-marimo 拡張
```

## ローカルで開発・プレビュー

```bash
# 1) 環境構築（uv を使う場合）
uv sync

# 2) プレビュー（http://localhost:4321）
uv run quarto preview

# 3) 静的サイト生成（_site/ に出力）
uv run quarto render
```

`venv` を使う場合：

```bash
python -m venv .venv
source .venv/bin/activate
pip install marimo numpy matplotlib qiskit qiskit-aer
quarto render
```

## Qiskit ノートブックを自分の PC で実行

```bash
uv run marimo edit notebooks/01_qubit_superposition.py
uv run marimo edit notebooks/02_entanglement.py
```

## 技術メモ（Quarto × marimo）

- 公式連携は **`marimo-team/quarto-marimo`** 拡張（`{python .marimo}` セル → marimo islands）。
- ブラウザ上は Pyodide（WASM）で実行されるため、**numpy / matplotlib のみ**を使う方針。
- **Qiskit は Rust ベースで WASM 非対応** → サイト内デモは自作の numpy シミュレータ（`lib/sim.py`）で再現。
- レッスンの背景セルは `{{< include ../lib/sim_cell.qmd >}}` で共有（WASM ではローカル import が保証されないため自己完結）。
- 依存は各ドキュメントの frontmatter `pyproject`（TOML）で宣言。ビルド時は uv、閲覧時は micropip で解決。

## デプロイ

- GitHub Pages 用ワークフロー `.github/workflows/gh-pages.yml` 付き。
- `main` に push すると自動で `_site/` が GitHub Pages に公開されます。
- リポジトリ設定で **Settings → Pages → Source: GitHub Actions** を選択してください。

## ライセンス

- 本教材の文書・画像は **CC BY 4.0**（出典明記で自由利用可）。
- コードは Apache-2.0（quarto-marimo に合わせた例）。

---

Planned & designed based on an OpenAI gpt-oss 120B generated draft.
