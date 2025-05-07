import pandas as pd
import numpy as np 

# Data from MAVISp - BRCA2
df = pd.read_csv("BRCA2-simple_mode.csv")

# Columns of interest
cols = [
    "Mutation", 
    "HGVSp", 
    "HGVSg", 
    "Mutation sources", 
    "Stability (FoldX5, alphafold, kcal/mol)", 
    "Stability (Rosetta Cartddg2020, alphafold, kcal/mol)",
    "Stability (RaSP, alphafold, kcal/mol)",
    "Stability classification, alphafold, (Rosetta, FoldX)",
    "Stability classification, alphafold, (RaSP, FoldX)",
    "Local Int. (Binding with SEM1_AFmulti, heterodimer, FoldX5, kcal/mol)",
    "Local Int. (Binding with SEM1_AFmulti, heterodimer, Rosetta Talaris 2014, kcal/mol)",
    "Local Int. classification (SEM1_AFmulti)",
    "AlloSigma2 predicted consequence - pockets and interfaces",
    "ClinVar Variation ID",
    "ClinVar Interpretation",
    "ClinVar Review Status",
    "DeMaSk delta fitness",
    "DeMaSk Shannon entropy",
    "DeMaSk log2 variant frequency",
    "DeMaSk predicted consequence",
    "GEMME Score",
    "GEMME Score (rank-normalized)",
    "AlphaMissense pathogenicity score",
    "AlphaMissense classification",
    "EVE score",
    "EVE classification (25% Uncertain)",
    "Experimental data (AVENGERS, Functional (AVENGERS,strict))",
    "Experimental data classification (AVENGERS, Functional (AVENGERS,strict))",
    "Experimental data (AVENGERS, Functional (AVENGERS,permissive))",
    "Experimental data classification (AVENGERS, Functional (AVENGERS,permissive))",
    "References"
    ]

selected_df = df[cols]

# Load selected mutations from iteraction range
muts_path = "../mutations_selections/muts_interaction_site.csv"
muts_df = pd.read_csv(muts_path)

# Add mutation format column for compatible with MAVISp dataframe
muts_df["Mutation"] = muts_df["ref_aa"] + muts_df["aa_position"].apply(str) + muts_df["alt_aa"]

# Get mutations info from MAVISp dataframe
mavisp_muts = muts_df[["aa_position","ref_aa","alt_aa","Mutation"]].merge(selected_df, how="left", on="Mutation")

# Save
mavisp_muts.to_csv("MAVISp_selected_mutations.csv", index=False)