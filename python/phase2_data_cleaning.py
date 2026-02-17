import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "business_performance_data.xlsx.xlsx"
)

df = pd.read_excel(file_path)

df.columns = (
    df.columns.str.lower()
    .str.strip()
    .str.replace(" ", "_")
)

df = df.drop_duplicates()

output_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_business_performance.csv"
)

os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print("✅ Phase 2 completed successfully")
