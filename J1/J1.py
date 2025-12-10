import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J1/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

# Part 1
position = 50
for line in data:
    rotation_dir = line[0]
    rotation_nb = int(line[1:])
    if rotation_dir == 'L':
        position -= rotation_nb
        if position < 0:
            while position < 0:
                position += 100
    else:
        position += rotation_nb
        if position >= 100:
            while position >= 100:
                position -= 100
    if position == 0:
        total_1 += 1

print("Total part 1: ", total_1)

# Part 2

position = 50
for line in data:
    start = position
    counted = False
    rotation_dir = line[0]
    rotation_nb = int(line[1:])
    if rotation_dir == 'L':
        position -= rotation_nb
        if position < 0:
            while position < 0:
                position += 100
                total_2 += 1
            if start == 0:
                total_2 -= 1
            if position == 0 and not counted:
                counted = True
    else:
        position += rotation_nb
        if position >= 100:
            while position >= 100:
                position -= 100
                total_2 += 1
            if start == 0:
                total_2 -= 1
            if position == 0 and not counted:
                counted = True
    if position == 0 and not counted:
        total_2 += 1
        
print("Total part 2: ", total_2)