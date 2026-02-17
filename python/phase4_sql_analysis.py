import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(
    BASE_DIR,
    "database",
    "business_performance.db"
)

conn = sqlite3.connect(db_path)

# 1️⃣ Sales & Profit by Region
query_region = """
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM business_performance
GROUP BY region
ORDER BY total_sales DESC;
"""

region_summary = pd.read_sql(query_region, conn)
print("\n📊 Sales & Profit by Region")
print(region_summary)

# 2️⃣ Profit Margin by Category
query_margin = """
SELECT
    category,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_percent
FROM business_performance
GROUP BY category
ORDER BY profit_margin_percent DESC;
"""

profit_margin = pd.read_sql(query_margin, conn)
print("\n📈 Profit Margin by Category (%)")
print(profit_margin)

# 3️⃣ Top 5 Products by Profit
query_top_products = """
SELECT
    product,
    ROUND(SUM(profit), 2) AS total_profit
FROM business_performance
GROUP BY product
ORDER BY total_profit DESC
LIMIT 5;
"""

top_products = pd.read_sql(query_top_products, conn)
print("\n🏆 Top 5 Products by Profit")
print(top_products)

# 4️⃣ Monthly Sales Trend
query_monthly = """
SELECT
    substr(order_date, 1, 7) AS month,
    ROUND(SUM(sales), 2) AS monthly_sales
FROM business_performance
GROUP BY month
ORDER BY month;
"""

monthly_sales = pd.read_sql(query_monthly, conn)
print("\n📅 Monthly Sales Trend")
print(monthly_sales)

conn.close()

print("\n✅ Phase 4 completed successfully")
