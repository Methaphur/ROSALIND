"""
Consensus and Profile
"""

# read_fasta from GC
def read_fasta(file):
    sequences = {}
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                seq_id = line[1:].strip()
                sequences[seq_id] = ''
            else:
                sequences[seq_id] += line.strip()
    return sequences


# Getting profile matrix and storing in a dictionary
def get_profile_matrix(sequences):
    n = len(sequences[list(sequences.keys())[0]])
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    for seq in sequences.values():
        for i in range(len(seq)):
            profile[seq[i]][i] += 1
    return profile


def get_consensus(profile):
    consensus = ''
    for i in range(len(profile['A'])):
        max_count = 0
        max_nucleotide = ''
        for nucleotide, counts in profile.items():
            if counts[i] > max_count:
                max_count = counts[i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide
    return consensus

def output_profile_matrix(profile):
    for nucleotide, counts in profile.items():
        print(f'{nucleotide}:', *counts)

file = 'rosalind_cons.txt'
sequences = read_fasta(file)
profile = get_profile_matrix(sequences)
consensus = get_consensus(profile)

# print(consensus)
# output_profile_matrix(profile)

# Writing output to file
with open('output.txt', 'w') as f:
    f.write(f'{consensus}\n')
    for nucleotide, counts in profile.items():
        f.write(f'{nucleotide}: {" ".join(map(str, counts))}\n')
    