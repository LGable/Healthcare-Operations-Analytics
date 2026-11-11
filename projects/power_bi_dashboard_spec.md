# Operations Performance Dashboard | Implementation Brief

**Type:** Synthetic Power BI design specification. Not a live PBIX or a copy of any employer dashboard.

## Intended audience

Owner/operator, finance administrator, consulting team lead. Recommended four pages:

1. **Executive pulse:** collections received, receivables outstanding, payroll exposure, revenue/cost trend, client satisfaction.
2. **Revenue cycle:** claim aging buckets, paid/denied/pending, payer type, collection lag and exception flags.
3. **Workforce and productivity:** staff utilization, visits/cases per FTE, missing documentation, schedule coverage.
4. **Quality:** satisfaction, documentation-completion rates, follow-through and trend annotations.

## Suggested synthetic schema

`fact_weekly_operations(week_id, claims_collected, unpaid_claims, payroll_spend, reports_completed, satisfaction_pct, productivity_index)`; optionally separate date, payer and staff dimension tables.

## Candidate measures (example DAX, adapt to proper data model)

```DAX
Collected Amount = SUM(fact_weekly_operations[claims_collected])
Payroll Amount = SUM(fact_weekly_operations[payroll_spend])
Mean Satisfaction = AVERAGE(fact_weekly_operations[satisfaction_pct])
Pending Claims = SUM(fact_weekly_operations[unpaid_claims])
```

## QA

Confirm date grain, row uniqueness, source mapping, complete payer definitions, and that financial figures do not double-count cash collections. Show selection/filter state, data provenance, and limitations on each page.

## Publication requirements

If a freelancer builds a PBIX, require source data to remain synthetic, measure definitions and screenshots to be present, and calculations to be reconciled to independent reference values. State freelancer contribution transparently.
