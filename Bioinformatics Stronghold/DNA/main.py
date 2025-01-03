"""
Of course there are many ways to solve this, one can use a dictionary to store the count of each nucleotide.
Or one can use the count() method of the string to count the number of each nucleotide.
Or one can just increase the count of each nucleotide in a loop. (since we know there are only 4 nucleotides)
"""

# Read the input data
with open('rosalind_dna.txt', 'r') as f:
    dna = f.read().strip()

# Or you could directly copy the input string and paste it as a variable 

# Method 1 using dictionary
nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for n in dna:
    nucleotide_count[n] += 1

print(nucleotide_count['A'], nucleotide_count['C'], nucleotide_count['G'], nucleotide_count['T'])

# Method 2 using count() method

# The fancy python method of doing the same thing

print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')) 
