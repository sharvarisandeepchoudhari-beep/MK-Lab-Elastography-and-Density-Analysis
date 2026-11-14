from pathlib import Path
import pandas as pd

# Path to the input dataset
DATA_FILE = Path("data") / "2708_Elastography_Collated Data.xlsx"

df = pd.read_excel(
    DATA_FILE,
    sheet_name="All_data_unique_kpa"
)
# Drop duplicates
df = df.drop_duplicates(
    subset=['grp_1', 'intratumoral_Kpa_new']
)

# Calculate mean intratumoral value for each grp_1
df['IL_avg'] = df.groupby('grp_1')['intratumoral_Kpa_new'].transform('mean')
#df['AN_avg'] = df.groupby('grp_1')['peritumoral_KPa_new'].transform('mean')

df = df.drop_duplicates(
    subset=['grp_1', 'IL_avg']
)
df = df.dropna(
    subset=['grp_1', 'IL_avg']
)
# Save
df.to_excel('avg_il.xlsx', index=False)
#assuming that duplicates in IL values are human error since there are many files merged into one.
