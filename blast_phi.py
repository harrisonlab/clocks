from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIXML
from BCBio import GFF
from pyfaidx import Fasta
import gffutils


geneList=[]
from Bio import SeqIO

# this uses pyfaidx to indes the genome 
genes = Fasta('vd.fasta')
db = gffutils.FeatureDB('vd', keep_order=True)

with open('vd_hits.txt','r') as f:
    for line in f:
        word=line.split()
        scaf=word[0]
        gene=word[4]
        gene=gene[7:-2]
        start=int(word[5])-1
        end=int(word[6])
        strand=word[7]
    	#print scaf,gene,start,end,strand
	gene_seq= genes[scaf][start:end]
	gene_feature=db.region(seqid=scaf, start=start, end=end,featuretype='CDS')
  	seq_exons = []
  	
  	
    #print gene_sequence
	print "NEXT FEATURES"
	print list(gene_feature)
	print gene_seq
	


#Feature gene (supercont1.38:84406-84732[-]
#in_seq_file = "vd.fasta"
#in_seq_handle = open(in_seq_file)
#seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
#in_seq_handle.close()

#gene_feature.sequence(genes, use_strand=True)
#print start
#subregion=  list(db.region(region=(scaf, start,end),featuretype='gene',completely_within=False)) 		
#subregion= list(db.region(region=(scaf, start,end),featuretype='gene',completely_within=False)) 		
#print subregion

#out_file = "vd_seq.gff"
#out_handle = open(out_file, "w")

#new_dict = {}
#in_file = "vd.gff3"
#in_handle = open(in_file)
#for rec in GFF.parse(in_handle, base_dict=seq_dict):
    #GFF.write(rec, out_handle)
#	print len(rec.features)
##	new_dict[rec.id] = rec
#in_handle.close()

#print len(new_dict)
#key1 = new_dict.keys()[0]
#print len(new_dict[key1].features)

#gffutils.Feature.sequence(fasta)


#Providing initial sequence records
#GFF records normally contain annotation data, while sequence information is available in a separate FASTA formatted file. The GFF parser can add annotations to existing records. First parse the sequence file with SeqIO, then feed the resulting sequence dictionary to the GFF parser:
#from BCBio import GFF
#from Bio import SeqIO
 







#blastp_hits = NcbiblastpCommandline(query="vd_hit_seq.fasta", db="phibase", evalue=0.001,outfmt=5, out="vd_blast_hit.xml")
#result_handle = open("vf_blast_hit.xml")
#blast_records = NCBIXML.parse(result_handle)
#for alignment in blast_records.alignments:
#	for hsp in alignment.hsps:
#        if hsp.expect < E_VALUE_THRESH:
#        	print('****Alignment****')
#            print('sequence:', alignment.title)
#            print('length:', alignment.length)
#            print('e value:', hsp.expect)             
#            print(hsp.query[0:75] + '...')
#            print(hsp.match[0:75] + '...')
#            print(hsp.sbjct[0:75] + '...')