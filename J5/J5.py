import numpy as np
from tqdm import tqdm

total_1 = 0
total_2 = 0
__path__ = './J5/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
        

# Part 1
fresh_ingredients = []
add_ingredients = True
for line in tqdm(data) :
    if line == '' :
        add_ingredients = False
        continue
    if add_ingredients :
        fresh_ingredients.append([int(line.split('-')[0]), int(line.split('-')[1])])
    else :
        test = int(line)
        for i_start, i_end in fresh_ingredients :
            if i_start <= test <= i_end :
                total_1 += 1
                break

print("Total part 1: ", total_1)

# Part 2

print("Total part 2: ", total_2)