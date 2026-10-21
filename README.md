# CodePF

Personal repository of Pedro Fatecha: programming practice, small experiments, and coursework from the Georgia Tech **Online Master of Science in Analytics (OMSA)**.

Topics covered include linear algebra, algorithms, data engineering and performance benchmarking, statistical and analytics modeling, and SQL.

**Languages and tools:** Python (Jupyter notebooks, pandas, Polars, DuckDB, Flask) · R · SQL · C++ · SSIS · LaTeX

## Repository structure

```
CodePF/
├── 00_Config/                  # Shared configuration (Databricks bundle, data-profiling output)
├── 01_Programing/              # Self-study and practice
│   ├── Algorithms/             # Algorithm exercises, image-to-pixel conversion, DataFrame→JSON helper
│   ├── Linear Algebra/         # Linear algebra notebooks
│   ├── DuckDB/                 # DuckDB vs. Polars vs. pandas speed test (has its own README)
│   ├── Data Integration practice/  # SQL Server Integration Services (SSIS) project + mock data
│   ├── Programming_training/C++/   # C++ and Python computing exercises
│   └── SQL/                    # SQL practice queries
├── 02_OMSA_GT/                 # Georgia Tech OMSA coursework
│   ├── ISYE6501_IntrotoAnalyticsModeling/  # Homework 1–11 (01_Data, 02_Script, 03_Output)
│   ├── CSE6040_ComputingDataAnalysis/      # Course notebooks (01_Data, 02_Notebooks)
│   └── MGT6203DataAnalyticsinbusiness/     # R homework and training notebooks
└── 03_Small_Implementations/
    └── calculator_app/         # Minimal Flask calculator web app
```

## Highlights

| Project | Description |
|---|---|
| [DuckDB speed test](01_Programing/DuckDB/1.duckdb_speed_test/) | Benchmarks pandas, Polars and DuckDB generating a 1M-person / 10M-position dataset, using `pytest-benchmark`. |
| [ISYE 6501 homework](02_OMSA_GT/ISYE6501_IntrotoAnalyticsModeling/) | Analytics-modeling assignments; rendered HTML reports are in `03_Output/`. |
| [CSE 6040 notebooks](02_OMSA_GT/CSE6040_ComputingDataAnalysis/02_Notebooks/) | Python fundamentals, efficiency and readability exercises. |
| [MGT 6203 scripts](02_OMSA_GT/MGT6203DataAnalyticsinbusiness/ScriptsR/) | R-based business analytics homework (notebooks + PDF exports). |
| [Calculator app](03_Small_Implementations/calculator_app/) | Flask app with a `/calculate` JSON endpoint and an HTML front end. |

## Getting started

```sh
git clone https://github.com/pedrofatecha/CodePF.git
cd CodePF
python3 -m venv .venv && source .venv/bin/activate
pip install jupyter pandas numpy matplotlib
```

Most content is Jupyter notebooks. Open them with `jupyter lab` or in VS Code. R notebooks need an R kernel (IRkernel).

**DuckDB benchmark** – see its [README](01_Programing/DuckDB/1.duckdb_speed_test/README.md):

```sh
cd 01_Programing/DuckDB/1.duckdb_speed_test
pip install -r requirements.txt
```

**Calculator app:**

```sh
pip install flask
python 03_Small_Implementations/calculator_app/app.py
# then open http://127.0.0.1:5000
```

## Note on coursework

The files in `02_OMSA_GT/` are my own submissions, shared as a portfolio. If you are currently enrolled in these courses, follow Georgia Tech's academic honor code.
