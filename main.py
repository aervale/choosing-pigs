from matplotlib import pyplot as plt
import numpy as np
import math
import random
import itertools


numberOfPigs = 1700
count = list(itertools.islice(itertools.count(1), numberOfPigs))
winners = []

values = [0]*numberOfPigs
names = count

def trial():
    pigs = list(itertools.islice(itertools.count(1), numberOfPigs))
    
    def removePigs(size):
        oddPigs = list(itertools.islice(pigs, 0, None, 2))
        pigs.remove(oddPigs[math.floor(random.random()*len(oddPigs))])
        if size> 2:
            removePigs(size-1)
        else:
            winners.append(pigs[0])
    removePigs(numberOfPigs)

    
    
for i in range(10000): 
    trial()

for winner in winners:
    values[winner-1] = values[winner-1]+1

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.plot(names, values)
