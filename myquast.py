import Bio
from Bio import SeqIO

max_contig = 0
contigs_length = []
sum_length = 0


with open("contigs.fa", "r") as contigs_fasta:
    my_data = SeqIO.parse("contigs.fa", "fasta")

## calculate total length of contigs
contig_sum = sum(len(record) for record in SeqIO.parse("contigs.fa", "fasta"))

## calculate number of contigs
contig_count = list(SeqIO.parse("contigs.fa", "fasta"))
len(contig_count)

## calculate length of longest contig
for record in SeqIO.parse("contigs.fa", "fasta"):
    if len(record) > max_contig:
        max_contig = len(record)
list_contigs = []
for record in my_data:
    list_contigs.append(len(record))
    list_contigs.sort()


N50_thresh = (contig_sum/2)
N50_value = 0
N50_list = []

for i in list_contigs:
    if N50_value + i < N50_thresh:
        N50_value = N50_value + i
        N50_list.append(i)
    elif N50_value + i >= N50_thresh:
        N50_list.append(i)
        break

print('Number of contigs: ', len(contig_count))
print('Total length: ',contig_sum)
print('Length of longest contig: ',max_contig)
print('N50: ' + str(max(N50_list)))


exit()
