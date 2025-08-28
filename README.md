# Mutation Analysis Project Overview 

Report: [📄 View the full documentation (PDF)](docs/report.pdf)

This project focuses on the analysis of protein mutations and their effects on structural stability and binding affinity. It is divided into four key components:

1. **PDB Miner**  
   Extracts and processes relevant `.pdb` structures for analysis. It ensures that input files are properly formatted and trimmed for downstream applications.

2. **Stability Analysis**  
   Utilizes **MutateX** and **FoldX** to evaluate the impact of mutations on protein stability by calculating changes in folding free energy (ΔΔG).

3. **Complex Binding Free Energies**  
   Assesses how mutations affect the interaction energy between proteins in a complex. Results are used to identify critical residues at the binding interface.

4. **CabFlex (Conformational Flexibility)**  
   Explores mutations with uncertain effects by generating multiple structural models using CabFlex. MutateX is rerun on these models to estimate mutation impact with higher robustness.
