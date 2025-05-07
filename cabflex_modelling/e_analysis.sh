#!/bin/bash

echo "model,residue,avg,std,min,max" > high_ddg.csv
echo "model,residue,avg,std,min,max" > low_ddg.csv

for i in {0..9}; do
  file="dat_files/selfmutation_energies${i}.dat"

  # ddG >= 1 kcal/mol
  awk '$2 >= 1 && $1 !~ /^#/ {
    printf "model_%d,%s,%.6f,%.6f,%.6f,%.6f\n", idx, $1, $2, $3, $4, $5
  }' idx="$i" "$file" >> high_ddg.csv

  # ddG <= -1 kcal/mol
  awk '$2 <= -1 && $1 !~ /^#/ {
    printf "model_%d,%s,%.6f,%.6f,%.6f,%.6f\n", idx, $1, $2, $3, $4, $5
  }' idx="$i" "$file" >> low_ddg.csv
done

