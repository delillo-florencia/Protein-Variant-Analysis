# import the UniProt data source class
from cancermuts.datasources import UniProt
from cancermuts.datasources import cBioPortal, COSMIC
from cancermuts.table import Table
# create the corresponding uniprot object

up = UniProt()

# get the sequence for the protein
seq = up.get_sequence('P51587', upid='BRCA2_HUMAN')

# this prints the downloaded protein sequence
print(seq)

#cb = cBioPortal()
#cb.add_mutations(seq, metadata=['cancer_type', 'cancer_study', 'genomic_mutations'])

cosmic = COSMIC(database_files='/data/databases/cosmic-v95/CosmicMutantExport.tsv',
	            database_encoding=['latin1'])
tbl = Table()

# generate pandas data frame
df = tbl.to_dataframe(seq)

#COSMIC
df.to_csv("metatable_.csv")
