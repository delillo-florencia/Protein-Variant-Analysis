import pandas as pd

df1=pd.read_csv("/home/projects/22117_proteins_2025/projects/group5_project/classified_single_mode_check.csv")
df2=pd.read_csv("/home/projects/22117_proteins_2025/projects/group5_project/classified_ensemble_mode.csv")

id_cols = ['WT residue type', 'chain ID', 'Residue #'] 

df1_sorted = df1.sort_values(by=id_cols).reset_index(drop=True)
df2_sorted = df2.sort_values(by=id_cols).reset_index(drop=True)

mutation_cols = [col for col in df1.columns if col not in id_cols]
mismatches = []

for idx in range(len(df1_sorted)):
    row1 = df1_sorted.iloc[idx]
    row2 = df2_sorted.iloc[idx]
    residue_id = f"{row1['WT residue type']}_{row1['chain ID']}_{row1['Residue #']}"
    
    for col in mutation_cols:
        val1 = row1[col]
        val2 = row2[col]
        if val1 != val2:
            mismatches.append({
                'Residue': residue_id,
                'AA mutation': col,
                'Single_mode': val1,
                'Ensemble_mode': val2
            })

mismatches_df = pd.DataFrame(mismatches)

if mismatches_df.empty:
    print(" All mutation effects match between the two DataFrames.")
else:
    print("Differences found in the following mutations:")
    print(mismatches_df)