import gffutils

f = open("vd_motifs.txt",'r')
for line in f.readlines():
	values=line.split('\t')
	scaf=values[0]
	m_start=int(values[1])
	m_end=int(values[2])
	motif=values[3]
	m_dir=values[4].strip()
	#print values[0],values[1],values[2],values[3],values[4]
	#print scaf,m_start,m_end,motif,m_dir
	a_fwd=1000
	#load the database
	db = gffutils.FeatureDB('vd', keep_order=True)
	record={}
	subregion={}
	
	if m_dir == '+':
		#print "Here +"
		subregion=  list(db.region(region=(scaf, m_start,m_end+a_fwd),featuretype='CDS',completely_within=False)) 		
		if len(subregion)>0:
			record=subregion[0]
		else:
			record=0
	elif m_dir == '-':
		#print "Here -"
		subregion=  list(db.region(region=(scaf, m_end-a_fwd,m_end),featuretype='CDS',completely_within=False))
		if len(subregion)>0:
			sub_val=len(subregion)-1
			record=subregion[sub_val]
		else:
			record=0
	else:
		print "Error"
		break
		
	if record ==0:
		#print "No hit"
		next
	else:
	#SELECT ONLY FIRST HIT IMMEDIATELY DOWNSTREAM
		if record.strand == '+' and m_dir == '+':
			upstream=record.start-m_end
			if upstream<0:
				next
			else:
				print record.id,motif,m_start,upstream,record['ID'],record.start,record.end,record.strand
		elif record.strand == '-' and m_dir == '-':
			upstream=(record.end-m_end)*-1
			if upstream<0:
				next
			else:
				print record.id,motif,m_start,upstream,record['ID'],record.start,record.end,record.strand
		else:
			#print "Strands incorrect"
			next
f.close()