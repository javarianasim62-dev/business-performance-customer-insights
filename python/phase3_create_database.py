import pandas as pd
import sqlite3
import os

# 1. Paths
csv_path = r"C:\Users\maria\Desktop\Business_Performance_Customer_Insights\data\processed\cleaned_business_performance.csv"
db_path = r"C:\Users\maria\Desktop\Business_Performance_Customer_Insights\sql\business_performance.db"

# 2. Safety check
if not os.path.exists(csv_path):
    raise FileNotFoundError("Cleaned CSV file not found. Run Phase 2 first.")

# 3. Load cleaned data
df = pd.read_csv(csv_path)

# 4. Create database & table
conn = sqlite3.connect(db_path)

df.to_sql(
    name="business_performance",
    con=conn,
    if_exists="replace",
    index=False
)

# 5. Verify table creation
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

conn.close()

print("Phase 3 completed: Database & table created successfully")
