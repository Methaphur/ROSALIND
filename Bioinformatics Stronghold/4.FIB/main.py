"""
We approach this problem by using the Fibonacci sequence. The number of rabbit pairs in each generation is equal to the sum of the number of rabbit pairs in the previous two generations. We can represent this as a recurrence relation:
The recurrence relation for the number of rabbit pairs in each generation is:
F(n) = F(n-1) + k * F(n-2)
"""

def recurrence_relation(months, litter_size):
    if months == 1 or months == 2:
        return 1
    else:
        return recurrence_relation(months - 1, litter_size) + litter_size * recurrence_relation(months - 2, litter_size)
    
# Now we apply dynamic programming to solve the problem

def rabbit_pairs(months, litter_size):
    rabbit_population = [0] * months
    rabbit_population[0] = 1
    rabbit_population[1] = 1
    for month in range(2, months):
        rabbit_population[month] = rabbit_population[month - 1] + litter_size * rabbit_population[month - 2]
    return rabbit_population[months - 1]

months = 5
litter_size = 3
print(rabbit_pairs(months, litter_size))

# Readind data from file
with open('rosalind_fib.txt', 'r') as f:
    months, litter_size = map(int, f.readline().split())

# Writing data to file
with open('output.txt', 'w') as f:
    f.write(str(rabbit_pairs(months, litter_size)))
