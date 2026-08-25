from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "saas_customers.csv"
OUT = ROOT / "outputs" / "charts"
OUT.mkdir(parents=True, exist_ok=True)


def load_data():
    df = pd.read_csv(DATA, parse_dates=["signup_date", "churn_date"])
    df["monthly_revenue"] = df["monthly_fee"]
    df["is_active"] = df["status"].eq("Active")
    df["is_churned"] = df["status"].eq("Churned")
    return df


def main():
    df = load_data()
    active = df[df["is_active"]]

    mrr = active["monthly_revenue"].sum()
    arr = mrr * 12
    customers = len(df)
    active_customers = len(active)
    churned = int(df["is_churned"].sum())
    churn_rate = churned / customers * 100
    revenue_at_risk = df.loc[df["is_churned"], "monthly_revenue"].sum()

    print("SaaS Revenue & Churn Analysis")
    print("=" * 35)
    print(f"Customers: {customers:,}")
    print(f"Active customers: {active_customers:,}")
    print(f"Churned customers: {churned:,}")
    print(f"MRR: ${mrr:,.0f}")
    print(f"ARR: ${arr:,.0f}")
    print(f"Customer churn rate: {churn_rate:.1f}%")
    print(f"Monthly revenue at risk: ${revenue_at_risk:,.0f}")

    plan = df.groupby("plan").agg(
        customers=("customer_id", "count"),
        churned=("is_churned", "sum"),
        active_mrr=("monthly_revenue", lambda x: x[df.loc[x.index, "is_active"]].sum()),
    )
    plan["churn_rate_pct"] = plan["churned"] / plan["customers"] * 100
    print("\nPlan analysis:\n", plan.sort_values("churn_rate_pct", ascending=False))

    plt.figure(figsize=(9, 5))
    sns.barplot(data=plan.reset_index(), x="plan", y="active_mrr")
    plt.title("Active MRR by Subscription Plan")
    plt.xlabel("Plan")
    plt.ylabel("Monthly Recurring Revenue ($)")
    plt.tight_layout()
    plt.savefig(OUT / "mrr_by_plan.png", dpi=160)
    plt.close()

    plt.figure(figsize=(9, 5))
    sns.barplot(data=plan.reset_index(), x="plan", y="churn_rate_pct")
    plt.title("Customer Churn Rate by Subscription Plan")
    plt.xlabel("Plan")
    plt.ylabel("Churn Rate (%)")
    plt.tight_layout()
    plt.savefig(OUT / "churn_rate_by_plan.png", dpi=160)
    plt.close()

    segment = df.groupby("segment").agg(
        customers=("customer_id", "count"),
        churned=("is_churned", "sum"),
        active_mrr=("monthly_revenue", lambda x: x[df.loc[x.index, "is_active"]].sum()),
    )
    segment["churn_rate_pct"] = segment["churned"] / segment["customers"] * 100
    segment.to_csv(OUT / "segment_analysis.csv")
    plan.to_csv(OUT / "plan_analysis.csv")

    print("\nCharts and summary tables saved to outputs/charts/")


if __name__ == "__main__":
    main()
