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

fresh_ingredients_ranges = []
add_ingredients = True
for line in tqdm(data) :
    if line == '' :
        add_ingredients = False
        break
    if add_ingredients :
        start, end = line.split('-')
        start = int(start)
        end = int(end)
        # print(f"Processing range: {start}-{end}")
        included = False

        # Merge start 
        for range_start, range_end in fresh_ingredients_ranges :
            if start > range_end or end < range_start :
                continue
            if start >= range_start and end <= range_end :
                included = True
                break
            if start > range_start :
                start = range_start
            if end < range_end :
                end = range_end
            fresh_ingredients_ranges.remove((range_start, range_end))
        # Merge end
        for range_start, range_end in fresh_ingredients_ranges :
            if start > range_end or end < range_start :
                continue
            if start >= range_start and end <= range_end :
                included = True
                break
            if end < range_end :
                end = range_end
            fresh_ingredients_ranges.remove((range_start, range_end))
        if not included :
            fresh_ingredients_ranges.append((start, end))
        # print(f"fresh_ingredients_ranges: {fresh_ingredients_ranges}")
                
for range_start, range_end in fresh_ingredients_ranges :
    total_2 += range_end - range_start + 1

print("Total part 2: ", total_2)