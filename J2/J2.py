import numpy as np
from tqdm import tqdm

total_1 = 0
total_2 = 0
__path__ = './J2/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

ranges = data[0].split(',')
ranges = [list(map(int, r.split('-'))) for r in ranges]       

# Part 1

for range_start, range_end in tqdm(ranges, desc="Processing all ranges, Part 1"):
    for number in tqdm(range(range_start, range_end + 1), desc=f"Processing range {range_start}-{range_end}", leave=False):
        str_num = str(number)
        len_nb = len(str_num)
        if len_nb % 2 != 0:
            continue
        first_half = str_num[:len_nb//2]
        second_half = str_num[len_nb//2:]
        if first_half == second_half:
            total_1 += number

print("Total part 1: ", total_1)

# Part 2

print("Total part 2: ", total_2)