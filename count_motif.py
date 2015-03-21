import re
from Bio import SeqIO
handle = open("vd.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
	print record.id,len(record.seq)
	stringseq= ''.join(record.seq)
	#matchObj = re.search( r'ATG', stringseq)
	#matchObj = re.search( r'[GC]TACA[CG]TA', stringseq)
	matchObj = re.search( r'G[CGA]CAGCCA', stringseq)
	#matchObj = re.search( r'G[AG]CGGGA', stringseq)
	#matchObj = re.search( r'GC[AG]CTAAC', stringseq)

	if matchObj:
   			print " Match", record.id ,matchObj.group()
	else:
  	 print "No match!!"


handle.close()