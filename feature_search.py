from BCBio import GFF
from Bio import SeqIO
 
in_seq_file = "nc.fasta"
in_seq_handle = open(in_seq_file)
seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
in_seq_handle.close()

in_file = "nc.gff3"
limit_info = dict(
        gff_id = ["7.25"],
        gff_type = ["CDS"])

in_handle = open(in_file)

for rec in GFF.parse(in_handle, limit_info=limit_info):
   print rec.features[0]
in_handle.close()

 
