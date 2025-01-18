"""
Combing Through The Haystack
"""

def find_motif(DNA, motif):
    positions = []
    for i in range(len(DNA) - len(motif) + 1):
        if DNA[i:i + len(motif)] == motif:
            positions.append(i + 1)
    
    return positions

print(*find_motif('GATATATGCATATACTT', 'ATAT'))

with open('rosalind_subs.txt', 'r') as f:
    DNA = f.readline().strip()
    motif = f.readline().strip()
    positions = find_motif(DNA, motif)

# Writing output to file
with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, positions)))