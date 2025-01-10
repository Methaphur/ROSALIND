""""
We iterate through both the strings simulatenously and compare what all characters are different
"""

def hamming_distance(s, t):
    count = 0    
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

def hamming(s, t):  # one liner because why not
    return sum([1 for i in range(len(s)) if s[i] != t[i]])

# Read the input data
with open('rosalind_hamm.txt', 'r') as file:
    s = file.readline().strip()
    t = file.readline().strip()

print(hamming_distance(s, t))