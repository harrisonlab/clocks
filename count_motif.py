import re
from Bio import SeqIO
handle = open("vd.fasta", "rU")
for record in SeqIO.parse(handle, "fasta") :
	print record.id,len(record.seq)
	stringseq= ''.join(record.seq)
	#matchObj = re.search( r'ATG', stringseq)
	#matchObj = re.search( r'[GC]TACA[CG]TA', stringseq)
	#matchObj = re.findall( r'G[CGA]CAGCCA', stringseq)
	#matchObj = re.search( r'G[AG]CGGGA', stringseq)
	#matchObj = re.search( r'GC[AG]CTAAC', stringseq)
	pattern=r'G[CGA]CAGCCA'
	regex = re.compile(pattern, re.IGNORECASE)
	for match in regex.finditer(stringseq):
		print "%s: %s" % (match.start(), match.group())

	


handle.close()