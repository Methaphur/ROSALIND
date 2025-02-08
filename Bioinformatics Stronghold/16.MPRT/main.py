import requests
import re

"""
Finding a Protein Motif
"""


def fetch_fasta(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    fasta = response.text
    return ''.join(fasta.split('\n')[1:])


"N-glycosylation motif is N{P}[ST]{P}"

def find_motif(sequence):
    motif_positions = []
    for i in range(len(sequence) - 3):
        if (sequence[i] == 'N' and
            sequence[i + 1] != 'P' and
            (sequence[i + 2] == 'S' or sequence[i + 2] == 'T') and
            sequence[i + 3] != 'P'):
            motif_positions.append(i + 1)
    return motif_positions

with open('test.txt', 'r') as file:
    for line in file:
        uniprot_id = line.strip()
        fasta_sequence = fetch_fasta(uniprot_id.split('_')[0])  
        motif_positions = find_motif(fasta_sequence)
        if motif_positions:
            print(uniprot_id)
            print(*motif_positions)

# with open('rosalind_mprt.txt', 'r') as file, open('output.txt', 'a') as output_file:
#     for line in file:
#         uniprot_id = line.strip()
#         fasta_sequence = fetch_fasta(uniprot_id.split('_')[0])  
#         motif_positions = find_motif(fasta_sequence)
#         if motif_positions:
#             output_file.write(f"{uniprot_id}\n")
#             output_file.write(' '.join(map(str, motif_positions)) + '\n')
