# Mutation Analysis Pipeline using MutateX and FoldX

This part performs mutation analysis on protein complexes using **MutateX** and **FoldX**, including energy estimation and classification of mutations.

---

### 1. Copy PDB Files to Server
Copy your `.pdb` files to the desired server directory, e.g., `complex_binding`.

### 2. Navigate to Project Directory
```bash
cd complex_binding
```

### 3. Run MUTATEX Singe mode
To run MutateX in single mode:
```bash
nohup mutatex AF_trimmed_BRCA_DSS1_final.pdb \
  -p 4 \
  -m mutation_list.txt \
  -x /home/ctools/foldx/foldx \
  -f suite5 \
  -R repair_runfile_template.txt \
  -M mutate_runfile_template.txt \
  -q poslist.txt \
  -L -l -v -C none -B \
  -I interface_runfile_template.txt &
```
### 4. Generate energy tables and heatmaps
Check `analysis.sh `for reference commands.

#### 4.1 Convert ΔΔG to .csv format
```bash
ddg2excel -p AF_trimmed_BRCA_DSS1_final.pdb \
  -l mutation_list.txt \
  -q poslist.txt \
  -d results/interface_ddgs/final_averages/A-B/ \
  -F csv
```
#### 4.2 Generate heatmap
```bash
ddg2heatmap -p AF_trimmed_BRCA_DSS1_final.pdb \
  -l mutation_list.txt \
  -q poslist.txt \
  -d results/interface_ddgs/final_averages/A-B/

```
This will generate energies.csv.
### Classify Mutations
Use check_energy.py to classify mutations. You need to input the energies.csv file, adjust the residues list and set corresponding thresholds.

### 5. Run Ensemble Mode for Uncertain mutations
If there are uncertain mutations, we can generate CabFlex models and rerun MutateX but in ensemble mode. Make sure you poslist.txt to include only uncertain mutations.
```bash

nohup mutatex model_*.pdb \
  -p 3 \
  -x /home/ctools/foldx/foldx \
  -m mutation_list.txt \
  -q poslist.txt \
  -f suite5 \
  -R repair_runfile_template.txt \
  -M mutate_runfile_template.txt \
  -c -L -l -v -C none -B \
  -I interface_runfile_template.txt &

```
### 6. Compare Single vs Ensemble Mode


Repeat the analysis and classification steps. Then, compare outputs using compare_results.py. Check results make sense or explore the complex using PyMol for explaining the results.