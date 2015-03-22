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
	fpatterns=(pattern1,pattern2,pattern3,pattern4)
	for pat in fpatterns:
		regex = re.compile(pat, re.IGNORECASE)
		for match in regex.finditer(stringseq):
			print "%s\t %s\t %s\t %s\t %s\t %s\t" % (record.id, match.start(),match.end(), match.group(),'+',pat)
	pattern5=r'TA[CG]TGTA[GC]'
	pattern6=r'TGGCTG[TCG]C'
	pattern7=r'TCCCG[CT]G'
	pattern8=r'GTTAG[CT]GC'
	rpatterns=(pattern5,pattern6,pattern7,pattern8)
	for pat in rpatterns:
		regex = re.compile(pat, re.IGNORECASE)
		for match in regex.finditer(stringseq):
			print "%s\t %s\t %s\t %s\t %s\t %s\t" % (record.id,match.start(),match.end(), match.group(),'-',pat)
		
handle.close()