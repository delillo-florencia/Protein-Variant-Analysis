# Stability Analysis Pipeline using MutateX and FoldX

This part performs stability analysis on protein complexes using **MutateX** and **FoldX**, including energy estimation and classification of mutations.

---

### 1. Copy PDB Files to Server
Copy your `.pdb` files to the desired server directory, e.g., `stability`.

### 2. Navigate to Project Directory
```bash
cd stability
```

### 3. Run MUTATEX Singe mode
To run MutateX in single mode:
```bash
nohup mutatex single-mode/BRCA_alone_ids_fixed.pdb \
  -p 4 \
  -m mutation_list.txt \
  -x /home/ctools/foldx/foldx \
  -f suite5 \
  -R single-mode/epair_runfile_template.txt \
  -M single-mode/mutate_runfile_template.txt \
  -q single-mode/poslist.txt \
  -L -l -v -B
```
### 4. Generate energy tables and heatmaps for single mode

#### 4.1 Convert ΔΔG to .csv format
```bash
ddg2excel -p single-mode/BRCA_alone_ids_fixed.pdb \
  -l single-mode/mutation_list.txt \
  -q single-mode/poslist.txt \
  -d single-mode/results/mutations_ddgs/final_averages \
  -o energies_single
  -F csv
```
#### 4.2 Generate heatmap
```bash
ddg2heatmap -p single-mode/BRCA_alone_ids_fixed.pdb \
  -l single-mode/mutation_list.txt \
  -q single-mode/poslist.txt \
  -d single-mode/results/mutaitons_ddgs/final_averages
  -o heatmap_single

```
This will generate energies-single.csv and corresponding heatmap.
### 4.3 Classify Mutations
Use classify_mutation.py to examine which residues should be run for an ensemble mode. This script classifies each mutation into one of four categories:

- **Stabilising:** ΔΔG ≤ -3 kcal/mol
- **Neutral:** -2 kcal/mol < ΔΔG < 2 kcal/mol
- **Uncertain:** 2 kcal/mol ≤ ΔΔG < 3 kcal/mol or -3 kcal/mol ≤ ΔΔG < -2 kcal/mol
- **Destabilising:** ΔΔG ≥ 3 kcal/mol

```bash
python classify_mutation.py --single energies.single.csv
```
The script will print out classified mutations. You should re-run an ensemble-mode on the uncertain residues.

### 5. Run Ensemble Mode for Uncertain mutations
If there are uncertain mutations, we can generate CabFlex models and rerun MutateX but in ensemble mode. Make sure you poslist.txt to include only uncertain mutations.
```bash

nohup mutatex ensemble-mode/model_{0-9}.pdb \
  -p 4 \
  -x /home/ctools/foldx/foldx \
  -m ensemble-mode/mutation_list.txt \
  -q ensemble-mode/poslist.txt \
  -f suite5 \
  -R ensemble-mode/repair_runfile_template.txt \
  -M ensemble-mode/mutate_runfile_template.txt \
  -c -L -l -v -B \

```
### 5. Generate energy tables and heatmaps for ensemble mode

#### 5.1 Convert ΔΔG to .csv format
```bash
ddg2excel -p ensemble-mode/model_0.pdb \
  -l ensemble-mode/mutation_list.txt \
  -q ensemble-mode/poslist.txt \
  -d ensemble-mode/results/mutations_ddgs/final_averages \
  -o energies_ensemble
  -F csv
```
#### 5.2 Generate heatmap
```bash
ddg2heatmap -p ensemble-mode/model_0.pdb \
  -l ensemble-mode/mutation_list.txt \
  -q ensemble-mode/poslist.txt \
  -d ensemble-mode/results/mutaitons_ddgs/final_averages
  -o heatmap_ensemble
```

### 6. Classify Mutations
Use classify_mutation.py to classify energies into mentioned above categories. With two inputs, the script performs the comparision of both modes.

```bash
python classify_mutation.py --single energies-single.csv --ensemble energies-ensemble.csv
```
The script will print out final comparision between single and ensemble mode.

> Remember to check that results make sense and explore the complex using PyMol for explaining the results.
