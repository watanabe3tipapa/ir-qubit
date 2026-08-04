# DEV-MEMO.md

Quarto × marimo による「量子技術」教材＆LP（ランディングページ）構築メモ。

## 目的

gpt-oss 120B による生成案をベースに、Nielsen & Chuang に着想を得た
「中学生でも量子コンピュータの概念をつかめる」学習キットを、**Quarto + marimo** で
Web 上にインタラクティブに公開する。

- **LP（index.qmd）**: キットの紹介・学習コース一覧・CTA
- **教材（lessons/*.qmd）**: 概念解説 + ブラウザ上で動くインタラクティブ・デモ

## 環境

| ツール | バージョン | 備考 |
|---|---|---|
| Quarto | 1.9.37 | quarto-marimo は >= 1.9.20 必須 ✅ |
| uv | 0.11.31 | ✅ |
| marimo | 0.19.9 → >= 0.23.1 | quarto-marimo は >= 0.23.1 必須 → プロジェクト venv で解決 |
| Python | 3.12 / 3.13 | qiskit は 3.14 未対応のため 3.12/3.13 を利用 |

## 技術方針（重要）

1. **公式連携は `marimo-team/quarto-marimo` の Quarto engine extension**。
   `{python .marimo}` セルを `.qmd` に直接書き、ページ内に「marimo islands」として埋め込む。

2. **ブラウザ上では Pyodide（WASM）で実行**される。よって:
   - **qiskit は Rust ベースで WASM 非対応** → ページ内デモでは使えない。
   - ページ内デモは **numpy 製の自作状態ベクトル・シミュレータ**で実装（教育用・数十行）。
   - numpy / matplotlib は Pyodide 標準対応なのでブラウザで動く ✅
   - **ローカルファイルの import は WASM で保証されない** → シミュレータは
     各レッスンの背景セル（echo: false）に自己完結で埋め込む。

3. **依存関係の宣言**: `_quarto.yml` の `pyproject` に numpy / matplotlib を記載。
   ビルド時は uv サンドボックス、閲覧時は micropip でインストールされる。

4. **qiskit は学習者がローカル実行するノートブック（notebooks/*.py）として同梱**。
   サイト内には埋め込まない（WASM で動かないため）。

## 構成

```
ir-qubit/
├── DEV-MEMO.md               # 本ファイル
├── _quarto.yml               # website 設定 + pyproject
├── index.qmd                 # LP
├── lessons/
│   ├── 01-qubit.qmd          # Qubit とは何か
│   ├── 02-superposition.qmd  # 重ね合わせ
│   ├── 03-entanglement.qmd   # エンタングルメント
│   ├── 04-gates.qmd          # 量子ゲート入門
│   ├── 05-measurement.qmd    # 測定と確率
│   └── 06-algorithms.qmd     # 量子アルゴリズム（Deutsch-Jozsa / Grover）
├── worksheets.qmd            # ワークシート（印刷用）
├── notebooks/                # ローカル実行用 qiskit 版 marimo
│   ├── 01_qubit_superposition.py
│   └── 02_entanglement.py
├── _extensions/marimo/       # quarto add marimo-team/quarto-marimo
├── .github/workflows/gh-pages.yml
└── README.md
```

## シミュレータ仕様（背景セルに埋め込む）

- `2^n` 次元の複素ベクトルで量子状態を保持（状態ベクトルシミュレーション）
- ゲート: H, X, Z, CNOT（ユニタリ行列を適用）
- 測定: 確率分布 `|amplitude|^2` から shots 回サンプリング → ヒストグラム
- 状態表示: 振幅の大きさを棒グラフ / コインの喩えで表示

## 実装チェックリスト（完了 2026-08-04）

- [x] uv で venv 構築（marimo>=0.23.1, numpy, matplotlib, qiskit, qiskit-aer）
- [x] `quarto add marimo-team/quarto-marimo`（v0.4.5）
- [x] `_quarto.yml` 作成（render 対象を明示指定）
- [x] シミュレータ実装（numpy）→ `lib/sim.py` / `lib/sim_cell.qmd`
- [x] レッスン6本 + ワークシート
- [x] LP（index.qmd）
- [x] ローカル実行用 qiskit ノートブック2本
- [x] GitHub Pages workflow + README
- [x] `quarto render` / `quarto preview` で動作確認（全9ページ生成、HTTP 200）

## 実装時の発見（重要）

1. **pyproject はドキュメント frontmatter に TOML 形式で書く**
   - 例: `pyproject: | requires-python = ">=3.13" / dependencies = ["numpy", "matplotlib"]`
   - `_quarto.yml` のグローバル宣言は拡張 0.4.5 では各ドキュメントに伝播しない。
2. **`{{< include >}}` をコードフェンス内に置くと展開されない**
   - 背景セルはフェンスの外で `{{< include ../lib/sim_cell.qmd >}}` とする。
3. **1 つの .qmd 内ではセル間で変数名を重複させない**（marimo の MultipleDefinitionError）。
4. **qubit0 が最上位ビット**。`measure_counts` のラベルは反転しない（左 = qubit0）。
5. `init_state` は complex 配列の先頭要素を 1 にする（ゼロベクトルにしない）。
6. `lib/*.qmd` は render 対象から外す（単独ページとして誤生成されるため）。
7. WASM 実行のためローカル import は不可 → 背景セルは自己完結（include でソース一元管理）。
8. **matplotlib プロット内の文字は英字のみ**（Pyodide/WASM は日本語グリフ非対応で豆腐化する）。
   `set_title` / `xlabel` / `ylabel` / `legend` などは英語表記に統一。`mo.ui.*` の `label=` は HTML 描画なので日本語でOK。
9. シミュレータの編集後は `lib/sim_cell.qmd` を再生成する（python スクリプトでモジュール docstring・import を除去して `{.marimo}` ブロック化）。

## 動作確認コマンド

```bash
quarto render        # _site/ を生成
quarto preview       # ローカルプレビュー（marimo islands の動作確認）
```

## 注意・既知の制約

- WASM 実行のため、セル内では numpy / matplotlib のみを前提にする。
- 初回閲覧時は Pyodide とパッケージのダウンロードが発生する（数秒〜十数秒）。
- marimo islands は Chrome 推奨（Safari は WASM 性能が劣る）。
