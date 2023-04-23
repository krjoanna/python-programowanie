# Create the generator random_walk(start) for a 1D random walker. 
#If a position at a certain moment is x, then the next position can be x+1 or x-1 
#with equal probabilities. Find the final position after 100 moves (start=0). Repeat experiments.

from random import random
import random
def random_walk(start = 0):
    while True:
        yield start
        start += random.choice([1,-1])

lista = []
for i in range(10):
    rw = random_walk()
    for x in range (100):
        next(rw)
    lista.append(next(rw))

print(lista)