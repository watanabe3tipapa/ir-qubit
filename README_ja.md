<!-- badges -->
[![License](https://img.shields.io/github/license/watanabe3tipapa/ir-qubit.svg)](LICENSE)
[![Quarto](https://img.shields.io/badge/Quarto-1.9-1496cc?logo=quarto&logoColor=white)](https://quarto.org)
[![marimo](https://img.shields.io/badge/marimo-0.23+-6E4B9C)](https://marimo.io)
[![Python](https://img.shields.io/badge/Python-3.12%7C3.13-3776AB?logo=python&logoColor=white)](https://python.org)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-brightgreen.svg)](https://github.com/watanabe3tipapa/ir-qubit)
[![Last commit](https://img.shields.io/github/last-commit/watanabe3tipapa/ir-qubit/main.svg)](https://github.com/watanabe3tipapa/ir-qubit/commits/main)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-2ea44f)](https://watanabe3tipapa.github.io/ir-qubit/)

[English](README.md) | [日本語](README_ja.md)

# 量子コンピュータ入門キット

**「Qubitって何？」から始める、ブラウザで動く量子入門教材（インストール不要）。**

Quarto × marimo で作ったこのキットは、コインの例えと**動く回路シミュレーション**を
組み合わせることで、重ね合わせ・もつれ・量子アルゴリズムといった量子コンピュータの
基本概念を、中学生でも直感的につかめるように設計しました。

- サイト内のデモは**ブラウザ上（WebAssembly / Pyodide）**で動きます。インストール不要。
- スライダーやボタンを動かすだけで、確率とヒストグラムが**リアルタイムに再計算**されます。
- 本格的な量子 SDK **Qiskit** を使った marimo ノートブックも同梱しています。

## 動機

量子コンピュータは魅力的ですが、たいていの入門書は線形代数やディラック記法の知識を
前提としています。*Nielsen & Chuang* に着想を得て、式を書く前にスライダーを触って
コイン投げが「量子コイン」に変わる瞬間を体験できる場所を作りたい、と思って作りました。

このキットは OpenAI の LLM との**長い長い会話の末**に生まれた草案をもとにしています。
量子コンピュータにはまだまだ学ぶべきことが多く、内容は決して「正解」ではありません。
誤りや不十分な点があれば、ぜひご指摘ください。

## 特徴

- **ブラウザで動く** — デモは Pyodide（WASM）で実行。セットアップ不要
- **6本のインタラクティブ・レッスン** — Qubit、重ね合わせ、もつれ、ゲート、測定、アルゴリズム
- **ライブシミュレーション** — 状態ベクトルとヒストグラムがリアルタイムに再計算
- **印刷用ワークシート** — 授業や自習の復習に
- **Qiskit ノートブック** — 本格的な量子 SDK に触れる実験（ローカル実行）
- **自作 numpy シミュレータ** — 教育用の状態ベクトル・シミュレータ（`lib/sim.py`）
- **自動デプロイ** — GitHub Pages ワークフローが push のたびに最新サイトを公開

## スクリーンショット

<!-- スクリーンショットをここに追加 -->

実際のサイトはこちら: [量子コンピュータ入門キット](https://watanabe3tipapa.github.io/ir-qubit/)

## インストール

```bash
# 1) 環境構築（uv を使う場合）
uv sync

# または、通常の venv を使う場合
python -m venv .venv
source .venv/bin/activate
pip install marimo numpy matplotlib qiskit qiskit-aer
```

## 使い方

```bash
# ローカルプレビュー（http://localhost:4321）
uv run quarto preview

# 静的サイト生成（_site/ に出力）
uv run quarto render
```

Qiskit ノートブックを自分の PC で実行:

```bash
uv run marimo edit notebooks/01_qubit_superposition.py
uv run marimo edit notebooks/02_entanglement.py
```

> 技術メモ: ページ内デモは Pyodide（WASM）で実行されるため、**numpy / matplotlib
> のみ**を前提にしています。Qiskit は Rust ベースで WASM 非対応のため、サイト内の
> デモは自作の numpy シミュレータで再現し、Qiskit ノートブックはローカル実行用に
> 同梱しています。詳細は [DEV-MEMO.md](DEV-MEMO.md) を参照してください。

## コントリビューション

コントリビューションは大歓迎です！

1. リポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. [Pull Request](https://github.com/watanabe3tipapa/ir-qubit/pulls) を作成

## ライセンス

- **文書・画像**: [CC BY 4.0](LICENSE-CC-BY)
- **コード**: [Apache-2.0](LICENSE)

## 連絡先

GitHub: [https://github.com/watanabe3tipapa/ir-qubit](https://github.com/watanabe3tipapa/ir-qubit)
