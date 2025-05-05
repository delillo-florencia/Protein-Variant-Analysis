import pandas as pd


df=pd.read_csv("/home/projects/22117_proteins_2025/projects/group5_project/complex_binding/energies.csv")
residue_list = [2520, 2687,2790,2800,3036]
df_filt=df[df["Residue #"].isin(residue_list)]

margin = 0.15

# Function to classify mutation effect with uncertainty margin
def classify(value):
    if abs(value - 1) <= margin or abs(value + 1) <= margin:
        return value
    elif value <= -1:
        return 'stabilizing'
    elif value >= 1:
        return 'destabilizing'
    else:
        return 'neutral'

# Apply classification only to mutation score columns
classified_df = df_filt.copy()
classified_df.iloc[:, 3:] = df_filt.iloc[:, 3:].applymap(classify)

# Result: classified_df will have the same structure, but with mutation effects instead of numbers
print(classified_df)
classified_df.to_csv("classified_single_mode.csv",index=False)
