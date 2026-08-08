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
│   ├── 06-algorithms.qmd     # 量子アルゴリズム（Deutsch-Jozsa / Grover）
│   ├── 07-multiqubit.qmd     # 複数量子ビットとテンソル積
│   ├── 08-more-gates.qmd     # 量子ゲートの拡張（Y・S・T / SWAP / Toffoli）
│   ├── 09-circuits.qmd       # 量子回路の読み方・書き方（ベル / GHZ）
│   ├── 10-advanced-algorithms.qmd  # Shor / QFT / QPE / VQE
│   ├── 11-noise.qmd          # ノイズと誤り訂正（NISQ）
│   └── 12-applications.qmd   # 応用と将来展望
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
- ゲート: H, X, Y, Z, S, T, CNOT, SWAP, Toffoli（各ユニタリ行列を適用）
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
- [x] `quarto render` / `quarto preview` で動作確認（全15ページ生成、HTTP 200）
- [x] レッスン7〜12 追加（複数Qubit / ゲート拡張 / 回路読み書き / 定番アルゴリズム / ノイズ / 応用）
- [x] ワークシートを 12 レッスン対応に拡張（Q11〜Q16、実験4・5）

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

## 追録（2026-08-09）：レッスン7〜12 追加と総合検証

### 実装結果

- **シミュレータ拡張**: `lib/sim.py` / `lib/sim_cell.qmd` に `apply_y` / `apply_s` / `apply_t` / `apply_swap` / `apply_ccnot` を追加。
  SWAP は CNOT×3 の組み合わせ、Toffoli は `apply_cnot` と同じテンソル置換パターン（perm [c1, c2, t] → reshape(8, -1) → `s[[6,7]] = s[[7,6]]`）で実装。
- **新規レッスン 6 本**（`lessons/07`〜`12`）と、`_quarto.yml` navbar / `index.qmd` / `worksheets.qmd`（Q11〜Q16 など）を更新。

### 追記・発見

1. **同一 .qmd 内で複数の marimo セルがトップレベル `fig`/`ax` を定義すると `MultipleDefinitionError`**。
   レッスン10・12 で `fig_qft/ax_qft`、`fig_qpe/ax_qpe`、`fig_vqe/ax_vqe`、`fig_shor`、`fig_qml` とセルごとに一意な名前にする必要があった。
   対策: 各セルで `fig_<内容>` / `ax_<内容>` などの一意名を使う（「実装時の発見」item 3 の具体例）。
2. **S・T などの位相ゲートを `|0⟩` に掛けてもブロッホ球は回らない**（`|0⟩` は S/T の固有方向）。
   位相回転を「見せる」には **重ね合わせ状態 `|+⟩` から開始** する（レッスン8 で修正）。
   - `Y|+⟩` → ブロッホ球 x 軸反転（`|−⟩`）、確率 50/50 のまま
   - `S|+⟩` → 90° 位相回転、`T|+⟩` → 45° 位相回転
3. **`|0⟩` に S・T を掛けても位相はゼロ、確率も変動なし**。位相ゲートが「確率を変えず位相だけを変える」ことを示すには、初期状態を重ね合わせにする必要がある。
4. **レッスン本文の物理的整合性**は `|0⟩` ベースの単純な説明だと崩れる。デモと文をセットで検証する（例: レッスン8 の「確率は変わりません」という記述は Y では正しくない → Y は Pauli で反転ゲート）。
5. **`quarto render` 実行時の marimo セル実行でエラーが出ても、終了コード 0 の場合がある**（stderr に `MultipleDefinitionError` が出るだけ）。検証は `rg -c "MultipleDefinitionError"` や、生成 HTML の確認で把握するのが確実。

### 検証手法（繰り返し使えるチェック）

- `lib/sim.py` と `lib/sim_cell.qmd` の一致: `ast` で関数・行列の本文を比較（import 行のみ差分で OK）。
- 複数セルで定義される変数重複・未定義参照の静的解析。
- 各レッスンの marimo セルの中身をローカル Python（numpy）で実行して数値検証。
- `quarto render` 後に生成 HTML 中の `MultipleDefinitionError` の有無を `rg` で確認。

### 検証実施結果（2026-08-09）

- `quarto render`: exit 0、`MultipleDefinitionError` 0、Warning 0、15/15 ページ生成。
- 生成 HTML に marimo 埋め込み・ランタイムエラーなしを確認。
- 数値ロジック: H⊗H 一様分布、GHZ（|000⟩/|111⟩）、Toffoli/SWAP、QFT 確率総和、VQE 収束、ノイズモデル、S²=Z/T²=S を検証。
- リンク（全レッスンの `{{< include ../lib/sim_cell.qmd >}}`）、ワークシート Q11〜Q16 も確認。
