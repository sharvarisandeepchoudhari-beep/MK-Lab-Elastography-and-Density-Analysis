import pandas as pd

from pathlib import Path

DATA_FILE = Path("data") / "2708_Elastography_Collated Data.xlsx"

df = pd.read_excel(
    DATA_FILE,
    sheet_name="All_data_unique_kpa"
)

def fill_by_group(df, cols, group_col='grp_1'):
    df = df.copy()

    for col in cols:
        new_col = col + '_new'
        df[new_col] = None

        for i in range(1, len(df)):
            if df.at[i, group_col] == df.at[i-1, group_col]:
                val = df.at[i, col]
                prev_val = df.at[i-1, col]

                if val == prev_val:
                    df.at[i, new_col] = 'NA'
                elif val in ['NA', 'Not recorded']:
                    df.at[i, new_col] = 'NA'
                else:
                    df.at[i, new_col] = val
            else:
                df.at[i, new_col] = df.at[i, col]

    return df


# Columns to process
cols_to_process = [
    'contralateral_kpa',
    'adj_normal_kpa',
    'peritumoral_KPa',
    'intratumoral_Kpa'
]

# Read input dataset

# Generate grp_1 using the three grouping columns
df['grp_1'] = (
    df.groupby(
        ['file_number', 'date_of_birth', 'usg_date'],
        dropna=False
    ).ngroup() + 1
)

# Sort rows so records belonging to the same group are adjacent
df = df.sort_values('grp_1').reset_index(drop=True)

# Execute measurement processing
df = fill_by_group(df, cols_to_process)

# Count records

