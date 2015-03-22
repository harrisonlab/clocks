import re
from Bio import SeqIO
handle = open("vd.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
	#print record.id,len(record.seq)
	stringseq= ''.join(record.seq)
	pattern1=r'[GC]TACA[CG]TA'
	pattern2=r'G[CGA]CAGCCA'
	pattern3=r'G[AG]CGGGA'
	pattern4=r'GC[AG]CTAAC'
	patterns=(pattern1,pattern2,pattern3,pattern4)
	for pat in patterns:
		regex = re.compile(pat, re.IGNORECASE)
		for match in regex.finditer(stringseq):
			print "%s\t %s\t %s\t %s\t" % (record.id, match.start(),match.end(), match.group())
handle.close()