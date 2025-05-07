#!/bin/bash

# Define the folder path
PDB_FOLDER="/home/projects/22117_proteins_2025/projects/group5_project/group_5_cabflex/brac_complex/output_pdbs"

# Validate the folder exists
if [ ! -d "$PDB_FOLDER" ]; then
    echo "Error: Folder '$PDB_FOLDER' does not exist!"
    exit 1
fi

# Initialize counter
found_files=0

echo "Processing the following PDB files:"
echo "----------------------------------"

# Loop over all model_*.pdb files
for pdb in "$PDB_FOLDER"/model_*.pdb; do
    # Skip if the glob doesn't match actual files
    [ -f "$pdb" ] || continue
    
    # Get just the filename without path or extension
    base_name=$(basename "$pdb" .pdb)
    
    # Print which file is being processed
    echo "Processing: $base_name.pdb"
    
    # Run mutatex and save output to [filename].out
    echo "Output will be saved to: $base_name.out"
    nohup mutatex "$pdb" -p 4 -x /home/ctools/foldx/foldx -m mutation_list.txt -f suite5 -R repair_runfile_template.txt -M mutate_runfile_template.txt -c -L -l -v -s > "${base_name}.out" 2>&1 
    
    # Increment counter
    ((found_files++))
done

# Check if any files were found
if [ "$found_files" -eq 0 ]; then
    echo "No PDB files found matching model_*.pdb in '$PDB_FOLDER'"
    exit 1
fi

echo "----------------------------------"
echo "Successfully processed $found_files files"
echo "Output files saved with .out extension in '$PDB_FOLDER'"
