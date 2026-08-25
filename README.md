# SaaS Revenue & Churn Analysis

## Problem Statement

SaaS businesses need to continuously monitor recurring revenue and customer churn to understand growth and identify retention opportunities.

This project analyzes subscription data to answer:
- How much recurring revenue is generated?
- Which plans contribute the most revenue?
- What is the customer churn rate?
- Which plans have the highest churn?
- How much recurring revenue is exposed to churn?
- Which customer segments should receive retention attention?

## Approach

1. **Data Preparation** — Clean subscription records and standardize dates, plans, segments, and monthly fees.
2. **Revenue Analysis** — Calculate active customers, MRR, ARR, and revenue contribution by plan.
3. **Churn Analysis** — Identify churned customers and calculate overall and plan-level churn rates.
4. **Revenue-at-Risk Analysis** — Estimate recurring revenue associated with churned customers.
5. **Business Recommendations** — Translate the findings into practical retention priorities.

## Key Insights

Using the project dataset as of March 2026:
- **269 of 300 customers are active**, generating **$39,431 MRR** and approximately **$473,172 ARR**.
- Overall customer churn is **11.0%**.
- **Starter** has the highest churn rate at **12.3%**, followed by **Growth at 13.3%**; Growth has the highest churn rate among the larger recurring-revenue plans.
- **Enterprise** has the lowest churn rate at **3.4%**, making it the strongest retention segment.
- Professional and Enterprise together account for a large share of recurring revenue, so protecting these customers has a disproportionate revenue impact.
- Retention efforts should prioritize high-value accounts while addressing onboarding and product-value issues in higher-churn plans.

## Tech Stack

- **Python** — Analysis and business metrics
- **Pandas** — Data cleaning and transformation
- **NumPy** — Numerical analysis
- **Matplotlib / Seaborn** — Visualization
- **Jupyter Notebook** — Analysis workflow
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

### 3. Run the analysis

```bash
jupyter notebook
```

Open `notebooks/saas_revenue_churn_analysis.ipynb` and run the cells from top to bottom.

## Project Structure

```text
SaaS-Revenue-Churn-Analysis/
├── data/
│   └── saas_customers.csv
├── notebooks/
│   └── saas_revenue_churn_analysis.ipynb
├── outputs/
│   └── charts/
├── requirements.txt
└── README.md
```
