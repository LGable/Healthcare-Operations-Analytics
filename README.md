# Healthcare Operations Analytics

Synthetic, public-safe demonstrations of healthcare operations analysis, financial reasoning, capacity planning, and decision-support reporting.

## What this repository demonstrates

- Separating collections, revenue, capacity, labor exposure, and modeled productivity value.
- Translating operational questions into measurable indicators and scenario analyses.
- Designing a Power BI dashboard from a documented synthetic data model.
- Communicating assumptions, limitations, and appropriate interpretation of financial metrics.

## Projects

| Project | Demonstrates |
|---|---|
| [Revenue-cycle and payroll cash-flow modeling](projects/revenue_cycle_cashflow.md) | Collections, labor-capacity, and financing-cost separation |
| [Rehabilitation capacity and reimbursement scenario](projects/rehabilitation_capacity.md) | Payer mix, case volume, length-of-stay, and capacity sensitivity |
| [Power BI dashboard specification](projects/power_bi_dashboard_spec.md) | Dashboard design, measures, wireframe, and data dictionary |

## Data and reproducibility

- [`data/operations_synthetic.csv`](data/operations_synthetic.csv) is synthetic weekly operations data created for demonstration.
- No employer, patient, payer, payroll, or clinical records are included.
- Read the [data policy](DATA_POLICY.md) before interpreting any metric.
- From this repository directory, run:

```powershell
python scripts/generate_demo_data.py
python scripts/analyze_operations.py
```

## Interpretation limits

- Annualized claim collections are not additional profit.
- Modeled organizational payroll exposure is not an owned budget.
- Estimated productivity value does not imply reduced cash payroll.
- Scenario outputs are analytical demonstrations, not audited employer accounts or guaranteed savings.

## Repository map

```text
data/       Synthetic demonstration data
projects/   Case studies and dashboard specification
scripts/    Data-generation and analysis scripts
```

## Provenance

This repository combines portfolio demonstrations with historical professional context. Historical outcomes are distinct from synthetic results, which demonstrate analytical methods and do not establish effectiveness for a real organization.
