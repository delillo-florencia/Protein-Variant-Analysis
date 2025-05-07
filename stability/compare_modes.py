import argparse
import pandas as pd

def classify_stability(value):
    if value <= -3:
        return 'stabilising'
    elif -2 < value < 2:
        return 'neutral'
    elif 2 <= value < 3 or -3 <= value <= -2:
        return 'uncertain'
    elif value >= 3:
        return 'destabilising'
    else:
        return 'uncertain'

parser = argparse.ArgumentParser(description='Classify stability of protein mutations from one or two XLSX files.')
parser.add_argument('--single', required=True, help='Path to the first XLSX file (single mode)')
parser.add_argument('--ensemble', required=False, help='Path to the second XLSX file (ensemble mode)')
args = parser.parse_args()

stability_data1 = pd.read_excel(args.single)
stability_data1 = stability_data1.melt(id_vars=['WT residue type', 'chain ID', 'Residue #'], var_name='Mutation', value_name='ΔΔG')
stability_data1['Classification'] = stability_data1['ΔΔG'].apply(classify_stability)

if args.ensemble:
    
    stability_data2 = pd.read_excel(args.input2)
    stability_data2 = stability_data2.melt(id_vars=['WT residue type', 'chain ID', 'Residue #'], var_name='Mutation', value_name='ΔΔG')
    stability_data2['Classification'] = stability_data2['ΔΔG'].apply(classify_stability)

    comparison = pd.merge(stability_data1, stability_data2, on=['WT residue type', 'chain ID', 'Residue #', 'Mutation'], suffixes=('_Single', '_Ensemble'))
    print(comparison)
else:
    print(stability_data1)
