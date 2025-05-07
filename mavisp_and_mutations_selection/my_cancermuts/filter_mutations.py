import pandas as pd
import numpy as np

# Getting table of all mutations from cancermuts
path = "my_cancermuts/metatable.csv"

df = pd.read_csv(path)
df = df.drop(["Unnamed: 0"], axis=1)

# Getting range of interaction site between dds1
aa_range = range(2479, 3181 + 1)

# Getting mutations from interacting AAs range
selected_df = pd.DataFrame(columns = df.columns)

for aa in aa_range:
    selected_aa = df[(df["aa_position"] == aa) & (df["alt_aa"].notna())]
    selected_df = pd.concat([selected_df, selected_aa], ignore_index = True)

# Save
selected_df.to_csv("muts_interaction_site.csv", index=False)