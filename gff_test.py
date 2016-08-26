import gffutils

#from BCBio import GFF
#from Bio import SeqIO
#in_seq_file = "vd.fasta"
#in_seq_handle = open(in_seq_file)
#seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
#in_seq_handle.close()

#new_dict = {}
#in_file = "vd.gff3"
#in_handle = open(in_file)
#for rec in GFF.parse(in_handle, base_dict=seq_dict):
# 	new_dict[rec.id] = rec
#in_handle.close()
#out_file = "new_vd.gff"
#with open(out_file, "w") as out_handle:
#    GFF.write([rec], out_handle)
    



#MAKE SQLITE DATABASES FROM THE GFF FILES - NOTE, SEQ DATA NOT ATTACHED
def transform_func(x):
     # adds some text to the end of transcript IDs
     if 'transcript_id' in x.attributes:
         x.attributes['transcript_id'][0] += '_transcript'
     return x

#ENSEMBL issues workaround here: http://pythonhosted.org/gffutils/examples.html
#db = gffutils.create_db("nc.gff3","nc1",id_spec={'gene': 'gene_id', 'transcript': "transcript_id"}, merge_strategy="create_unique", transform=transform_func,keep_order=True)
db = gffutils.create_db("vd.gff3","vd",id_spec={'gene': 'gene_id', 'transcript': "transcript_id"}, merge_strategy="create_unique",transform=transform_func,keep_order=True)





