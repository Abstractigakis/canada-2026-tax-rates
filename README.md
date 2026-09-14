# Canada 2026 GST/HST, mileage, and payroll rates

Published 2026 Canadian GST/HST/PST, CRA mileage, CPP/CPP2, QPP, EI, TFSA, and RRSP figures. MIT JSON plus two CSVs.

**Not tax advice.** CRA, Finance Canada, ESDC, Retraite Québec, and Revenu Québec win if anything disagrees.

- Dataset page: https://abstractigakis.com/data
- Free calculators: https://abstractigakis.com/shop-tools
- Listed in [Awesome Public Datasets](https://github.com/awesomedata/apd-core/blob/master/core/Government/Canada-2026-Tax-Payroll-Rates.yml) (Government)
- Same files in [lead-machine-demo](https://github.com/Abstractigakis/lead-machine-demo) and [jsDelivr](https://cdn.jsdelivr.net/gh/Abstractigakis/lead-machine-demo/rates-2026.json)

## Files

| File | What |
| --- | --- |
| [`rates-2026.json`](rates-2026.json) | All rates, official sources, calculator URLs |
| [`sales-tax-2026.csv`](sales-tax-2026.csv) | GST / PST / HST by province and territory |
| [`payroll-2026.csv`](payroll-2026.csv) | CPP, CPP2, QPP, EI employee rates and maxes |

```bash
curl -s https://raw.githubusercontent.com/Abstractigakis/canada-2026-tax-rates/main/rates-2026.json
```

## Figures people search

- TFSA annual limit **$7,000**; unused room if eligible since 2009 **$109,000**
- RRSP dollar limit **$33,810**
- Mileage: **73¢ / 67¢** per km in the provinces; **77¢ / 71¢** in the territories
- CPP YMPE **$74,600**, employee **5.95%**, max **$4,230.45**; CPP2 **4%** to YAMPE **$85,000**
- EI **1.63%** on MIE **$68,900** outside Quebec
- Quebec QST **9.975% on the price excluding GST** (combined 14.975%)
- Nova Scotia HST **14%**

## Official sources

- [Which GST/HST rate](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html)
- [2026 automobile deduction limits](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html)
- [CPP rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)
- [EI rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html)
- [TFSA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/contributing/before.html)
- [RRSP / YMPE limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html)
- [Québec Pension Plan figures](https://www.retraitequebec.gouv.qc.ca/en/programs/quebec-pension-plan/quebec-pension-plan-figures)
