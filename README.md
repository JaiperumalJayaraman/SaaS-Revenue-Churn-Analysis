# SaaS Revenue & Churn Analysis

## Problem Statement

SaaS businesses need to monitor recurring revenue and customer churn to understand growth, identify high-risk customer groups, and prioritize retention efforts.

This project analyzes 100 customer subscription records to answer:
- How much recurring revenue is generated?
- Which plans contribute the most MRR?
- What is the customer churn rate?
- Which plans and segments have the highest churn?
- How much monthly revenue is exposed to churn?
- Where should retention efforts be prioritized?

## Approach

1. **Data validation** — Check duplicates, missing values, valid subscription fees, and churn/status consistency.
2. **Revenue analysis** — Calculate active Monthly Recurring Revenue (MRR) and Annual Recurring Revenue (ARR), then compare plans and customer segments.
3. **Churn analysis** — Derive active/churned status from `churn_date` and calculate overall, plan-level, and segment-level churn rates.
4. **Revenue-at-risk analysis** — Quantify monthly recurring revenue associated with churned customers.
5. **Business recommendations** — Convert the findings into practical retention priorities.

## Key Insights

Based on the verified 100-customer dataset:

- **MRR is $14,858**, equivalent to **$178,296 ARR**.
- **8 of 100 customers have churned**, giving an overall customer churn rate of **8.0%**.
- **Starter has the highest plan churn rate at 12.9%**, followed by Growth at 10.0%.
- **Enterprise has 0% observed churn** in this sample and contributes **$5,489 active MRR**.
- **SMB has the highest segment churn rate at 13.3%** and is also the largest segment with 60 customers.
- Churned customers represent **$692 in monthly recurring revenue at risk**.
- Revenue impact is concentrated in Starter ($196), Growth ($297), and Professional ($199) among the observed churned customers.

## Business Recommendations

- Strengthen onboarding and early product-value communication for **Starter and Growth** customers.
- Use proactive churn monitoring for **SMB** accounts because SMB is the only segment with observed churn in this sample.
- Protect high-MRR **Professional and Enterprise** accounts with proactive customer-success outreach.
- Track **MRR at risk alongside customer churn**, so retention work is prioritized by financial impact rather than customer count alone.

## Tech Stack

- **Python** — Analysis and business metrics
- **Pandas** — Data cleaning, transformation, and aggregation
- **Matplotlib** — Visualization
- **Jupyter Notebook** — Exploratory and end-to-end analysis
- **GitHub** — Version control and documentation

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/JaiperumalJayaraman/SaaS-Revenue-Churn-Analysis.git
cd SaaS-Revenue-Churn-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis script

```bash
python run_analysis.py
```

The script reads `data/saas_customers.csv` and writes KPI and plan/segment tables to `outputs/` and charts to `outputs/charts/`.

### 4. Open the notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/saas_revenue_churn_analysis.ipynb
```

Run the notebook from top to bottom to reproduce the analysis.

## Project Structure

```text
SaaS-Revenue-Churn-Analysis/
├── data/
│   └── saas_customers.csv
├── notebooks/
│   └── saas_revenue_churn_analysis.ipynb
├── src/
│   ├── __init__.py
│   └── saas_analysis.py
├── outputs/
│   ├── analysis_summary.md
│   ├── charts/
│   │   ├── mrr_by_plan.svg
│   │   ├── churn_rate_by_plan.svg
│   │   ├── revenue_by_segment.svg
│   │   ├── revenue_at_risk.svg
│   │   └── customer_status.svg
│   └── (generated CSV KPI summaries)
├── run_analysis.py
├── requirements.txt
└── README.md
```

## Limitations

This is a portfolio/business analytics project based on a small sample dataset. The results demonstrate the analytical workflow and should not be interpreted as production SaaS benchmarks.
