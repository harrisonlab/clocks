#Verticillium_clock
Looking for Neurospora crassa PAS domains in Verticillium dahliae. Especially focusing in the WC-2 PAS domain.


All work was performed in the following directory:
```bash
	mkdir -p /home/groups/harrisonlab/project_files/verticillium_dahliae/clocks
	cd  /home/groups/harrisonlab/project_files/verticillium_dahliae/clocks
	```
	
verticillium data is stored in /home/groups/harrisonlab/project_files/verticillium_dahliae/wilt

Look for PAS domains identified in Verticillium Interproscan 
```bash
	less ../wilt/gene_pred/interproscan/V.dahliae/53/53_interproscan.tsv 
```

All annotations with interproscan IPR000014 were identified using the following command:

```bash
	cat ../wilt/gene_pred/interproscan/V.dahliae/53/53_interproscan.tsv | grep 'IPR000014'| less
```
 
 If you want to look just the first column of the file:
 ```bash 
 	cat ../wilt/gene_pred/interproscan/V.dahliae/53/53_interproscan.tsv | grep 'IPR000014'| cut -f1 | less
```

To get rid of the repeated genes on the list:
```bash
	cat ../wilt/gene_pred/interproscan/V.dahliae/53/53_interproscan.tsv | grep 'IPR000014'| cut -f1 | sort | uniq | less
	```
	
To create a loop in order to perform the same with all the different strains of Verticillium
```bash
for Genome in $(ls  ../wilt/gene_pred/augustus/V.dahliae/); do
echo $Genome 
ls ../wilt/gene_pred/augustus/V.dahliae/"$Genome"/"$Genome"_aug_preds.gff
mkdir -p PAS_protein/V.dahliae/"$Genome"/
cat ../wilt/gene_pred/interproscan/V.dahliae/"$Genome"/"$Genome"_interproscan.tsv | grep 'IPR000014'| cut -f1 | sort | uniq > PAS_protein/V.dahliae/"$Genome"/"$Genome"_genes_containing_IPR000014.txt
done
```

Search command 
``` bash
	cat ../wilt/gene_pred/augustus/V.dahliae/51/51_aug_out.aa | sed '1,/g1497.t1/d' | sed '/>/q' | head -n-1 | less
	```
	
To create a loop to search for all the files and print the aa sequences:
```bash 
cat PAS_protein/V.dahliae/51/51_genes_containing_IPR000014.txt  | while read gene; do 
echo ">$gene"; 
cat ../wilt/gene_pred/augustus/V.dahliae/51/51_aug_out.aa | sed "1,/$gene/d" | sed '/>/q' | head -n-1
done | less
```

Create a loop to 
```bash
for Strain in $(ls  ../clocks/PAS_protein/V.dahliae/); do 
echo $Strain;
cat PAS_protein/V.dahliae/"$Strain"/"$Strain"_genes_containing_IPR000014.txt  | while read gene; do 
echo ">$gene"; 
cat ../wilt/gene_pred/augustus/V.dahliae/"$Strain"/"$Strain"_aug_out.aa | sed "1,/$gene/d" | sed '/>/q' | head -n-1
done > PAS_protein/V.dahliae/"$Strain"/"$Strain"_genes_containing_IPR000014.fasta 
done
	```
	
