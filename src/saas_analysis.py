from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "saas_customers.csv"
OUT = ROOT / "outputs"
CHARTS = OUT / "charts"
CHARTS.mkdir(parents=True, exist_ok=True)


def load_data():
    df = pd.read_csv(DATA, parse_dates=["start_date", "churn_date"])
    df["status"] = df["churn_date"].notna().map({True: "Churned", False: "Active"})
    df["is_active"] = df["status"].eq("Active")
    df["is_churned"] = df["status"].eq("Churned")
    return df


def main():
    df = load_data()
    active = df[df["is_active"]]
    churned = df[df["is_churned"]]

    mrr = active["monthly_fee"].sum()
    arr = mrr * 12
    customers = len(df)
    active_customers = len(active)
    churned_customers = len(churned)
    churn_rate = churned_customers / customers * 100
    revenue_at_risk = churned["monthly_fee"].sum()

    print("SaaS Revenue & Churn Analysis")
    print("=" * 35)
    print(f"Customers: {customers:,}")
    print(f"Active customers: {active_customers:,}")
    print(f"Churned customers: {churned_customers:,}")
    print(f"MRR: ${mrr:,.0f}")
    print(f"ARR: ${arr:,.0f}")
    print(f"Customer churn rate: {churn_rate:.1f}%")
    print(f"Monthly revenue at risk: ${revenue_at_risk:,.0f}")

    plan = df.groupby("plan").agg(
        customers=("customer_id", "count"),
        churned=("is_churned", "sum"),
        active_mrr=("monthly_fee", lambda x: x[df.loc[x.index, "is_active"]].sum()),
    )
    plan["churn_rate_pct"] = plan["churned"] / plan["customers"] * 100
    plan.to_csv(OUT / "plan_analysis.csv")

    segment = df.groupby("segment").agg(
        customers=("customer_id", "count"),
        churned=("is_churned", "sum"),
        active_mrr=("monthly_fee", lambda x: x[df.loc[x.index, "is_active"]].sum()),
    )
    segment["churn_rate_pct"] = segment["churned"] / segment["customers"] * 100
    segment.to_csv(OUT / "segment_analysis.csv")

    charts = [
        (plan["active_mrr"].sort_values(ascending=False), "Active MRR by Plan", "MRR ($)", "mrr_by_plan.png"),
        (plan["churn_rate_pct"].sort_values(ascending=False), "Customer Churn Rate by Plan", "Churn Rate (%)", "churn_rate_by_plan.png"),
        (segment["active_mrr"].sort_values(ascending=False), "Active MRR by Customer Segment", "MRR ($)", "revenue_by_segment.png"),
        (churned.groupby("plan")["monthly_fee"].sum().sort_values(ascending=False), "Monthly Revenue at Risk by Plan", "Revenue at Risk ($)", "revenue_at_risk.png"),
        (df["status"].value_counts(), "Customer Status", "Customers", "customer_status.png"),
    ]

    for series, title, ylabel, filename in charts:
        ax = series.plot(kind="bar", figsize=(9, 5))
        ax.set_title(title)
        ax.set_xlabel("")
        ax.set_ylabel(ylabel)
        plt.tight_layout()
        plt.savefig(CHARTS / filename, dpi=160)
        plt.close()

    pd.DataFrame({
        "metric": ["customers", "active_customers", "churned_customers", "mrr", "arr", "churn_rate_pct", "monthly_revenue_at_risk"],
        "value": [customers, active_customers, churned_customers, mrr, arr, churn_rate, revenue_at_risk]
    }).to_csv(OUT / "kpi_summary.csv", index=False)

    print("\nAnalysis outputs saved to outputs/.")


if __name__ == "__main__":
    main()
