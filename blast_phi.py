from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIXML

geneList=[]
from Bio import SeqIO
handle = open("vd.fasta", "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()


with open('vd_hits.txt','r') as f:
    for line in f:
        word=line.split()
        scaf=word[0]
        gene=word[4]
        gene=gene[7:-2]
        start=word[5]
        end=word[6] 
       # print scaf,gene,start,end
        #geneList.append(gene)







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