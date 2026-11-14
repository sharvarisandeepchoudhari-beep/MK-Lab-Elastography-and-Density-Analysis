import pandas as pd
from pathlib import Path

# Read input dataset
DATA_FILE = Path("data") / "input_dataset.xlsx"

df = pd.read_excel(
    DATA_FILE,
    sheet_name="2012_2022_filtered"
)

df = df.drop_duplicates('IDENTITY', keep='last')
df= df.loc[df['density']== 'a']
#df= df.loc[df['density']== 'b']
#df= df.loc[df['density']== 'c']
#df= df.loc[df['density']== 'd']
print(pd.crosstab(df['birad_benign_or_malignant'], df['bx_benign_or_malignant']))
