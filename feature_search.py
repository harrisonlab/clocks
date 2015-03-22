#from BCBio import GFF
#from Bio import SeqIO

#in_seq_file = "nc.fasta"
#in_seq_handle = open(in_seq_file)
#seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
#in_seq_handle.close()

#in_file = "nc.gff3"
#limit_info = dict(
#        gff_id = ["7.23"],
#        gff_type = ["CDS"])
#in_handle = open(in_file)

#for rec in GFF.parse(in_handle, limit_info=limit_info):
#   print rec.features[0]
#in_handle.close()
 
#to do- work out how to efficiently query gff for each motif location and ask whether it 
#upstream of a coding sequence- making sure that the orientation is correct 


import gffutils

scaf='7.23'

#need to get end first
motif="TEST"
m_start=7892
m_end=7899
a_fwd=1000
m_dir=-1


db = gffutils.FeatureDB('nc', keep_order=True)
record={}

if m_dir == 1:
	if len(subregion)>0:
		subregion=  list(db.region(region=(scaf, m_start,m_end+a_fwd),featuretype='CDS',completely_within=False)) 
		record=subregion[0]
	else:
		record=0
#NOTE WHEN THIS IS GOING THE 'OTHER' WAY SUBREGION[0] APPEARS TO SELECT THE FURTHEST AWAY
#WHEN THERE ARE >1 HIT, NOT THE NEAREST SO IT NEEDS ALTERING
else:
	subregion=  list(db.region(region=(scaf, m_end-a_fwd,m_end),featuretype='CDS',completely_within=False))
	if len(subregion)>0:
		sub_val=len(subregion)-1
		record=subregion[sub_val]
	else:
		record=0
 
if record ==0:
	print "No hit"
else:
#SELECT ONLY FIRST HIT IMMEDIATELY DOWNSTREAM
#for record in subregion :
	if record.strand == '+' and m_dir == 1:
		print "Motif",motif
		print "Motif start",m_start
		upstream=record.start-m_start
		print 'Motif upstream', upstream, "bp"
		print record['ID'],record.start,record.end,record.strand
		
	elif record.strand == '-' and m_dir == -1:
		print "Motif",motif
		print "Motif start",m_start
		print "Motif dir",m_dir
		upstream=(record.end-m_end)*-1
		print 'Motif upstream', upstream, "bp"
		print record['ID'],record.start,record.end,record.strand
	else:
		print "Strands incorrect"
	