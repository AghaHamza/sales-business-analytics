
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("superstore_sales.csv")

print("ORIGINAL SHAPE:", df.shape)

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# Convert dates
df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%m/%d/%Y",
    errors="coerce"
)

# Inspect duplicates
print("\nDUPLICATE ROWS:", df.duplicated().sum())
print(df[df.duplicated(keep=False)])

# Remove exact duplicates
df = df.drop_duplicates().copy()

# Validate data
print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nNEGATIVE SALES:", (df["sales"] < 0).sum())
print("NON-POSITIVE QUANTITIES:", (df["quantity"] <= 0).sum())

# Extract date features
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["year_month"] = df["order_date"].dt.to_period("M")

print("\nCLEANED SHAPE:", df.shape)
print("DATE RANGE:", df["order_date"].min(), "to", df["order_date"].max())

# Save cleaned data
df.to_csv("cleaned_superstore_sales.csv", index=False)


# ==========================================
# BUSINESS PERFORMANCE ANALYSIS
# ==========================================

print("\n========== BUSINESS KPIs ==========")

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_orders = len(df)
total_quantity = df["quantity"].sum()
profit_margin = (total_profit / total_sales) * 100

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Transaction Rows: {total_orders:,}")
print(f"Total Units Sold: {total_quantity:,}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")


# ==========================================
# SALES AND PROFIT BY CATEGORY
# ==========================================

category_performance = (
    df.groupby("category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
    .sort_values("total_sales", ascending=False)
)

category_performance["profit_margin_pct"] = (
    category_performance["total_profit"]
    / category_performance["total_sales"] * 100
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_performance.round(2))


# ==========================================
# VISUALIZATION 1: SALES BY CATEGORY
# ==========================================

category_performance["total_sales"].plot(
    kind="bar",
    figsize=(9, 5),
    title="Total Sales by Product Category",
    ylabel="Sales ($)",
    xlabel="Category"
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=150)
plt.show()


# ==========================================
# VISUALIZATION 2: PROFIT BY CATEGORY
# ==========================================

category_performance["total_profit"].plot(
    kind="bar",
    figsize=(9, 5),
    title="Total Profit by Product Category",
    ylabel="Profit ($)",
    xlabel="Category"
)

plt.axhline(y=0, color="black", linewidth=0.8)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_category.png", dpi=150)
plt.show()


# ==========================================
# NUMPY: IDENTIFY PROFITABLE CATEGORIES
# ==========================================

category_performance["performance"] = np.where(
    category_performance["total_profit"] > 0,
    "Profitable",
    "Loss-making"
)

print("\n========== CATEGORY STATUS ==========")
print(category_performance[
    ["total_profit", "performance"]
].round(2))

# Save category analysis
category_performance.to_csv("category_performance.csv")

print("\nCategory analysis and charts saved successfully!")

print("\nCleaned data saved successfully!")


# ==========================================
# SUB-CATEGORY PROFITABILITY ANALYSIS
# ==========================================

subcategory_analysis = (
    df.groupby("sub_category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
)

subcategory_analysis["profit_margin_pct"] = (
    subcategory_analysis["total_profit"]
    / subcategory_analysis["total_sales"] * 100
)

# Most profitable sub-categories
print("\n========== TOP 5 BY PROFIT ==========")
print(
    subcategory_analysis
    .sort_values("total_profit", ascending=False)
    .head(5)
    .round(2)
)

# Most loss-making sub-categories
print("\n========== BOTTOM 5 BY PROFIT ==========")
print(
    subcategory_analysis
    .sort_values("total_profit")
    .head(5)
    .round(2)
)

# Furniture-specific investigation
furniture = df[df["category"] == "Furniture"]

furniture_analysis = (
    furniture.groupby("sub_category")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
    .sort_values("total_profit")
)

print("\n========== FURNITURE ANALYSIS ==========")
print(furniture_analysis.round(2))

# Visualize profit by sub-category
subcategory_analysis["total_profit"].sort_values().plot(
    kind="barh",
    figsize=(10, 7),
    title="Profit by Product Sub-Category",
    xlabel="Total Profit ($)",
    ylabel="Sub-Category"
)

plt.axvline(x=0, color="black", linewidth=0.8)
plt.tight_layout()
plt.savefig("profit_by_subcategory.png", dpi=150)
plt.show()

subcategory_analysis.to_csv("subcategory_analysis.csv")

print("\nSub-category analysis saved successfully!")


# ==========================================
# MONTHLY SALES AND PROFIT TREND ANALYSIS
# ==========================================

monthly_analysis = (
    df.groupby("year_month")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum")
    )
)

# Convert monthly period labels into timestamps for plotting
monthly_analysis.index = monthly_analysis.index.to_timestamp()

print("\n========== MONTHLY PERFORMANCE ==========")
print(monthly_analysis.round(2))

# Find the strongest and weakest months
best_sales_month = monthly_analysis["total_sales"].idxmax()
worst_sales_month = monthly_analysis["total_sales"].idxmin()

best_profit_month = monthly_analysis["total_profit"].idxmax()
worst_profit_month = monthly_analysis["total_profit"].idxmin()

print("\nBest month by sales:", best_sales_month.strftime("%Y-%m"))
print("Lowest month by sales:", worst_sales_month.strftime("%Y-%m"))
print("Best month by profit:", best_profit_month.strftime("%Y-%m"))
print("Lowest month by profit:", worst_profit_month.strftime("%Y-%m"))

# Plot monthly sales
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_analysis.index,
    monthly_analysis["total_sales"],
    marker="o",
    linewidth=1.5
)
plt.title("Monthly Sales Trend (2014–2017)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.show()

# Plot monthly profit
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_analysis.index,
    monthly_analysis["total_profit"],
    marker="o",
    linewidth=1.5
)
plt.axhline(y=0, color="black", linewidth=0.8)
plt.title("Monthly Profit Trend (2014–2017)")
plt.xlabel("Month")
plt.ylabel("Profit ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_profit_trend.png", dpi=150)
plt.show()

# Save monthly results
monthly_analysis.to_csv("monthly_analysis.csv")

print("\nMonthly analysis saved successfully!")


# ==========================================
# REGIONAL PERFORMANCE ANALYSIS
# ==========================================

regional_analysis = (
    df.groupby("region")
    .agg(
        total_sales=("sales", "sum"),
        total_profit=("profit", "sum"),
        units_sold=("quantity", "sum")
    )
)

regional_analysis["profit_margin_pct"] = (
    regional_analysis["total_profit"]
    / regional_analysis["total_sales"] * 100
)

regional_analysis = regional_analysis.sort_values(
    "total_sales", ascending=False
)

print("\n========== REGIONAL PERFORMANCE ==========")
print(regional_analysis.round(2))

print("\nHighest sales region:",
      regional_analysis["total_sales"].idxmax())

print("Highest profit region:",
      regional_analysis["total_profit"].idxmax())

print("Highest margin region:",
      regional_analysis["profit_margin_pct"].idxmax())

# Visualize regional sales and profit
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

regional_analysis["total_sales"].plot(
    kind="bar", ax=axes[0], title="Sales by Region",
    ylabel="Sales ($)", xlabel="Region"
)

regional_analysis["total_profit"].plot(
    kind="bar", ax=axes[1], title="Profit by Region",
    ylabel="Profit ($)", xlabel="Region"
)

axes[0].tick_params(axis="x", rotation=0)
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig("regional_performance.png", dpi=150)
plt.show()

regional_analysis.to_csv("regional_analysis.csv")
