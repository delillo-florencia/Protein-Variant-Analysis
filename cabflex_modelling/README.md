# CABFlex Modeling Overview

1. **`CABFlex.sh`**  
   This script takes as input both BRCA2 structures—one in isolation and one in complex with DSS1. It generates 10 models for each input `.pdb` file using CABFlex.

2. **`model_eval.sh`**  
   This script takes the paths to the generated model files and performs a self-scan using MutateX on each model. For each one, it outputs a file containing the corresponding `ΔΔG` values.

3. **`e_analysis.sh`**  
   This script processes the `.dat` files produced in the previous step and converts them into a readable `.csv` format for downstream analysis.