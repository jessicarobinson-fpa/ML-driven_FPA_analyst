# ML-Driven FP&A Analyst -- Headcount Variance Analysis

An ML-driven headcount actuals-vs-forecast analysis project built on the CRISP-DM framework, adapted for FP&A at Entrata.

## Project Structure

```
lab/headcount_variance/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/               # Close File extracts, Domo pulls
│   ├── interim/           # Cleaned/joined tables
│   └── processed/         # Modeling-ready actuals vs forecast
├── notebooks/
│   ├── 01_business_understanding.ipynb   # Phase 1: Current process documentation
│   ├── 02_data_understanding.ipynb       # Phase 2: Data profiling (upcoming)
│   ├── 03_data_preparation.ipynb         # Phase 3: Data pipeline (upcoming)
│   ├── 04_analysis_and_modeling.ipynb    # Phase 4: Variance + predictive (upcoming)
│   └── 05_evaluation.ipynb              # Phase 5: Validation (upcoming)
├── src/
│   ├── config.py           # Paths, constants, department mappings
│   ├── data_io.py          # Domo + Close File loaders
│   ├── variance.py         # Variance calculation engine
│   ├── trends.py           # Trend/anomaly detection
│   └── forecasting.py      # Predictive model
├── reports/
│   ├── figures/
│   ├── tables/
│   └── executive_summary.md
├── jobs/                   # Automation (future phase)
└── logs/
```

## CRISP-DM Phases

| Phase | Notebook | Status |
|-------|----------|--------|
| 1. Business Understanding | `01_business_understanding.ipynb` | Complete |
| 2. Data Understanding | `02_data_understanding.ipynb` | Pending |
| 3. Data Preparation | `03_data_preparation.ipynb` | Pending |
| 4. Analysis & Modeling | `04_analysis_and_modeling.ipynb` | Pending |
| 5. Evaluation | `05_evaluation.ipynb` | Pending |

## Data Sources

- **ADP** -- Employee system of record (via Domo integration)
- **Domo** -- HC Upload Writeback card + department mapping
- **Adaptive Planning** -- Actuals, CWM, and Latest Forecast versions
- **Close File - Master** -- Office Connect reporting workbook
