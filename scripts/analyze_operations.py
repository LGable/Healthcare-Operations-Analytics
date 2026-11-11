from pathlib import Path
import csv, statistics
p=Path(__file__).resolve().parents[1]/'data'/'operations_synthetic.csv'
with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
assert len(rows)==52
for name in ['claims_collected_usd','payroll_spend_usd']:
 print(f'{name} (synthetic annual sum): ${sum(float(r[name]) for r in rows):,.2f}')
print('Synthetic average satisfaction:',round(statistics.mean(float(r['satisfaction_pct']) for r in rows),2),'%')
print('Caution: these are invented demonstration figures, not employer data.')
