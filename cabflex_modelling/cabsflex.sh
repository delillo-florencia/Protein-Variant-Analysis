#!/bin/bash

#VARIABLES
pdb='trimmed_BRCA.pdb'
medoids=10
montecarlo=30
annealing_cycles=10
verbosity=3
seed=10
output_name="trimmed_BRCA.pdb.out"


#1 deactivate conda env
#conda deactivate 

#2 activate CABS env
#source /home/ctools/CABS/bin/activate

#3 Run CABflex with desired parameters

nohup CABSflex -i "${pdb}" -k "${medoids}" -y "${montecarlo}" -a "${annealing_cycles}" -v "${verbosity}" -z "${seed}" -A & 