"""
Mendelian Inheritance
"""

def mendelian_inheritance(k, m, n):
    total = k + m + n
    prob = (
        (k / total) * ((k - 1) / (total - 1)) +
        2 * (k / total) * (m / (total - 1)) +
        2 * (k / total) * (n / (total - 1)) +
        (m / total) * ((m - 1) / (total - 1)) * 0.75 +
        2 * (m / total) * (n / (total - 1)) * 0.5
    )
    return prob


# print(mendelian_inheritance(2, 2, 2))  

with open('rosalind_iprb.txt', 'r') as f:
    k, m, n = map(int, f.readline().split())
    print(mendelian_inheritance(k, m, n))

