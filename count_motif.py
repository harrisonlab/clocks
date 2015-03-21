import re
from Bio import SeqIO
handle = open("vd.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
	print record.id,len(record.seq)
	stringseq= ''.join(record.seq)
	pattern1=r'[GC]TACA[CG]TA'
	pattern2=r'G[CGA]CAGCCA'
	pattern3=r'G[AG]CGGGA'
	pattern4=r'GC[AG]CTAAC'
	regex = re.compile(pattern2, re.IGNORECASE)
	for match in regex.finditer(stringseq):
		print "%s: %s" % (match.start(), match.group())

	


handle.close()