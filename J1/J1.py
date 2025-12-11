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
zero_last = False
go_to_0 = False
for line in data:
    tmp = position
    tmp2 = total_2
    rotation_dir = line[0]
    rotation_nb = int(line[1:])
    nb_total_turns = rotation_nb // 100
    total_2 += nb_total_turns
    rotation_nb = rotation_nb % 100

    if rotation_dir == 'L':
        position -= rotation_nb
        if position < 0 :
            position += 100
            if not zero_last :
                total_2 += 1
    else:
        position += rotation_nb
        if position > 100:
            position -= 100
            total_2 += 1
        if position == 100 :
            position = 0
            go_to_0 = True
            total_2 += 1
    if position == 0 and not go_to_0:
        zero_last = True
        total_2 += 1
    elif go_to_0 :
        zero_last = True
        go_to_0 = False
    else:
        zero_last = False
        
print("Total part 2: ", total_2)