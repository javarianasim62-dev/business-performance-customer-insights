import sqlite3
import pandas as pd
import os

# -----------------------------
# 1. Database path (VERY IMPORTANT)
# -----------------------------
db_path = r"C:\Users\maria\Desktop\Business_Performance_Customer_Insights\sql\business_performance.db"

# -----------------------------
# 2. Output folder
# -----------------------------
output_dir = r"C:\Users\maria\Desktop\Business_Performance_Customer_Insights\data\processed"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# 3. Connect to database
# -----------------------------
conn = sqlite3.connect(db_path)
print("Connected to database")

# -----------------------------
# 4. Check tables
# -----------------------------
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)
print("Tables in database:")
print(tables)

# -----------------------------
# 5. Query 1: Sales by Region
# -----------------------------
query_region = """
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales
FROM business_performance
GROUP BY region
ORDER BY total_sales DESC;
"""

region_sales = pd.read_sql(query_region, conn)
region_sales.to_csv(os.path.join(output_dir, "region_sales.csv"), index=False)
print("Saved: region_sales.csv")

# -----------------------------
# 6. Query 2: Monthly Sales
# -----------------------------
query_monthly = """
SELECT
    substr(order_date, 1, 7) AS month,
    ROUND(SUM(sales), 2) AS monthly_sales
FROM business_performance
GROUP BY month
ORDER BY month;
"""

monthly_sales = pd.read_sql(query_monthly, conn)
monthly_sales.to_csv(os.path.join(output_dir, "monthly_sales.csv"), index=False)
print("Saved: monthly_sales.csv")

# -----------------------------
# 7. Query 3: Top Products by Profit
# -----------------------------
query_profit = """
SELECT
    product,
    ROUND(SUM(profit), 2) AS total_profit
FROM business_performance
GROUP BY product
ORDER BY total_profit DESC
LIMIT 10;
"""

top_products_profit = pd.read_sql(query_profit, conn)
top_products_profit.to_csv(
    os.path.join(output_dir, "top_products_profit.csv"),
    index=False
)
print("Saved: top_products_profit.csv")

# -----------------------------
# 8. Close connection
# -----------------------------
conn.close()
print("Phase 5 completed successfully")
