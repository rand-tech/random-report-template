# random-report-template
[README (English)](README.md) | 解説記事: [怠けるLaTeX (pandasとgnuplot)](https://zenn.dev/rand0m/articles/the-lazy-latex) |  
repo: https://github.com/rand-tech/random-report-template

- tsvからLaTeXの表をコマンドひとつで生成できる
- tsvから(.texファイルの)図をコマンドひとつで生成できる

## requirements
- LaTeX
- Python
- pandas (python)
- gnuplot

## 使い方
詳しくは`showcase/report/final/lazy-LaTeX.pdf`を参照

```mermaid
flowchart LR
   gs(Google Spreadsheet) -- clipboard --> tsv(tsv file) -- make table.o --> table
   tsv -- make figure.o --> plotした図
```
(tsvファイルとして読み込むのはGoogle Spreadsheetsをコピーする際にtsvとして保存されるから)

## ディレクトリ構成
```
❯ tree
.
├── README.md
├── showcase
│   ├── Final
│   └── report
│       ├── Makefile -> ../../skelton-experiment/report/Makefile
│       ├── gnuplot-lua-tikz-common.tex -> ../../skelton-experiment/report/gnuplot-lua-tikz-common.tex
│       ├── gnuplot-lua-tikz.sty -> ../../skelton-experiment/report/gnuplot-lua-tikz.sty
│       ├── info.sty -> ../../skelton-experiment/report/info.sty
│       ├── out
│       │   ├── src
│       │   │   └── data
│       │   └── template.pdf
│       ├── preamble.sty -> ../../skelton-experiment/report/preamble.sty
│       ├── src
│       │   ├── 1mokuteki.tex
│       │   ├── 2genri.tex
│       │   ├── 3houhou.tex
│       │   ├── 4kekka.tex
│       │   ├── 5kousatu.tex
│       │   ├── data
│       │   │   ├── e_showcase.csv
│       │   │   ├── exp_1.gp
│       │   │   ├── latex_e_showcase.csv.tex
│       │   │   ├── make_table.py
│       │   │   └── showcase.tex
│       │   ├── img
│       │   │   └── showcaseimage.png
│       │   └── references.bib
│       └── template.tex
└── skelton-experiment
    ├── Final
    └── report
        ├── Makefile
        ├── gnuplot-lua-tikz-common.tex
        ├── gnuplot-lua-tikz.sty
        ├── info.sty
        ├── out
        │   ├── src
        │   │   └── data
        │   └── template.pdf
        ├── preamble.sty
        ├── src
        │   ├── 1mokuteki.tex
        │   ├── 2genri.tex
        │   ├── 3houhou.tex
        │   ├── 4kekka.tex
        │   ├── 5kousatu.tex
        │   ├── data
        │   │   └── make_table.py
        │   ├── img
        │   └── references.bib
        └── template.tex

```


