from pathlib import Path
import csv, random, math
random.seed(20261110)
p=Path(__file__).resolve().parents[1]/'data'/'operations_synthetic.csv';p.parent.mkdir(parents=True,exist_ok=True)
with p.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['week_id','claims_collected_usd','unpaid_claims_usd','payroll_spend_usd','reports_completed','satisfaction_pct','productivity_index'])
 for week in range(1,53):
  w.writerow([week,max(700,round(random.gauss(7500+30*math.sin(week/6),950))),max(0,round(random.gauss(15000-35*week,1900))),round(random.gauss(15900,850)),random.randint(4,7),round(max(65,min(99,random.gauss(86+week*.07,3))),1),round(max(.5,min(1.5,random.gauss(.91+week*.001,.08))),3)])
print('Regenerated SYNTHETIC file:',p)
