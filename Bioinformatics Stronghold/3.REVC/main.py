"""
Our task is to find the reverse complement of a DNA string.
We first read the DNA string from the file and then reverse the string.
Then we replace each nucleotide with its complement.
"""

# Replace each nucleotide with its complement
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def reverse_complement(dna):
    reverse_dna = dna[::-1] # Reverse the DNA string
    reverse_complement = "".join(complement[nucleotide] for nucleotide in reverse_dna)
    return reverse_complement

with open('rosalind_revc.txt', 'r') as file:
    input_dna = file.read().strip()


reverse_complement_dna = reverse_complement(input_dna)


with open('output.txt', 'w') as file:
    file.write(reverse_complement_dna)
