"""
We need to calculate the GC content of a DNA sequence. We also need to properly process the input data.
"""

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

def gc_content(sequence):
    gc = 0
    for base in sequence:
        if base in 'GC':
            gc += 1
    return gc / len(sequence) * 100


def highest_gc_content(sequences):
    highest_gc = 0
    highest_gc_id = ''
    for seq_id, sequence in sequences.items():
        gc = gc_content(sequence)
        if gc > highest_gc:
            highest_gc = gc
            highest_gc_id = seq_id
    return highest_gc_id, highest_gc


file = 'rosalind_gc.txt'
sequences = read_fasta(file)
highest_gc_id, highest_gc = highest_gc_content(sequences)

with open('output.txt', 'w') as f:
    f.write(f'{highest_gc_id}\n{highest_gc}')
