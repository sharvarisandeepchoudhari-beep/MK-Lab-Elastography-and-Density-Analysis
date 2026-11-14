import pandas as pd
from pathlib import Path

# Read input dataset
DATA_FILE = Path("data") / "input_rad_dataset.xlsx"

df = pd.read_excel(
    DATA_FILE,
    sheet_name="2012_2022_filtered"
)

# Drop duplicates
df = df.drop_duplicates("IDENTITY", keep="last")

# Convert age values to numeric
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Filter patients
df = df[df["bx_benign_or_malignant"] == "Not Aval"]

# Extract valid ages
age = df["age"].dropna()

# Calculate statistics
median = age.median()
q1 = age.quantile(0.25)
q3 = age.quantile(0.75)
iqr = q3 - q1

# Print results
print(f"Number of patients: {len(age)}")
print(f"Median (Q1–Q3): {median:.2f} [{q1:.2f}–{q3:.2f}]")
print(f"Interquartile range (IQR): {iqr:.2f}")
print(f"Mean ± SD: {age.mean():.2f} ± {age.std():.2f}")
