# clocks
Look for motifs from the Hurley PNAS paper in promoters of genes. 
Do some kind of comparison between N.crassa and V.d?

Note- for Biopython to read gff it needs 
`http://github.com/chapmanb/bcbb/tree/master/gff/`

and I had to upgrade distribute using:
`easy_install --user -U distribute`

and then install using:
`pip install bcbio-gff`

There were issues with doing this- pip was not picking up the local distribute install for some reason, so I ended up upgrading the global copy...
tried prepending ~/.local/lib/python2.7/site-packages to the PYTHONPATH:
`PYTHONPATH=$HOME/.local/lib/python2.7/site-packages:$PYTHONPATH`



Genomes downloaded from http://fungi.ensembl.org/Verticillium_dahliae/Info/Index?db=core
and http://fungi.ensembl.org/Neurospora_crassa/Info/Index

`ln -s /home/groups/harrisonlab/ref_genomes/fungi/v_dahliae/Verticillium_dahliae.GCA_000150675.1.25.dna.genome.fa vd.fasta`

`ln -s /home/groups/harrisonlab/ref_genomes/fungi/v_dahliae/Verticillium_dahliae.GCA_000150675.1.25.gff3 vd.gff3`

`ln -s /home/groups/harrisonlab/ref_genomes/fungi/n_crassa/Neurospora_crassa.ASM18292v1.25.dna.genome.fa nc.fasta`

`ln -s /home/groups/harrisonlab/ref_genomes/fungi/n_crassa/Neurospora_crassa.ASM18292v1.25.gff3 nc.gff3`


Note- fasta is hard-coded as I am in a hurry...

`python count_motif.py >nc_motifs.txt`

`python count_motif.py >vd_motifs.txt`


Develop script to parse gff for motifs in above list in putative promoters- drawing on http://biopython.org/wiki/GFF_Parsing

run (one time only)

`gff_test.py (again hard coded paths) to create SQLITE databases of gff files`

run (remember the hard coding)

`feature_search.py?vd_hits.txt` 

This will return a list of promoter motifs that have a gene upto 1k downstream of the promoter
 
