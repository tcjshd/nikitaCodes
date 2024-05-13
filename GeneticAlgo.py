import random

# Define the function to optimize
def f(x):
    return x ** 2

# Take user input for parameters
ps = int(input("Enter population size: "))
cl = int(input("Enter chromosome length: "))
mr = float(input("Enter mutation rate: "))
g = int(input("Enter number of generations: "))

# Generate initial population
pop = []
for _ in range(ps):
    c = [random.randint(0, 1) for _ in range(cl)]
    pop.append(c)

# Main loop for generations
for generation in range(g):
    # Calculate fitness for each chromosome
    fs = []
    for chromosome in pop:
        x = int("".join(map(str, chromosome)), 2)  # Convert chromosome to integer
        fitness = f(x)
        fs.append(fitness)

    # Select parents based on fitness
    pr = []
    for _ in range(ps):
        # Use roulette wheel selection
        tf = sum(fs)
        sp = random.uniform(0, tf)
        cf = 0
        for i, score in enumerate(fs):
            cf += score
            if cf >= sp:
                pr.append(pop[i])
                break

    # Crossover and mutation
    npop = []
    for i in range(0, ps, 2):
        p1, p2 = pr[i], pr[i + 1]
        cp = random.randint(1, cl - 1)
        ch1 = p1[:cp] + p2[cp:]
        ch2 = p2[:cp] + p1[cp:]
        
        # Apply mutation
        for j in range(cl):
            if random.random() < mr:
                ch1[j] ^= 1  # Flip the bit
            if random.random() < mr:
                ch2[j] ^= 1
        npop.append(ch1)
        npop.append(ch2)
    pop = npop

# Find the best chromosome in the final population
bc = pop[0]
bf = fs[0]
for i in range(1, ps):
    if fs[i] > bf:
        bc = pop[i]
        bf = fs[i]

# Print the results
bx = int("".join(map(str, bc)), 2)
print("Best chromosome:", bc)
print("Best x:", bx)
print("Best fitness:", bf)
