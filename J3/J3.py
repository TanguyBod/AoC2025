import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J3/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
        
# Part 1

def process_bank_p1(bank : str) -> int :
    # Find the max value index
    bank_list = [int(x) for x in bank.strip()]
    max_index = bank_list.index(max(bank_list))
    max_number = bank_list[max_index]
    bank_list[max_index] = 0
    # Case when max is the last element
    if max_index == len(bank_list) - 1 :
        # Find 2nd max
        second_max_index = bank_list.index(max(bank_list))
        second_max_number = bank_list[second_max_index]
        return int(str(second_max_number) + str(max_number))
    else :
        # Find max after max_index
        next_max_index = bank_list.index(max(bank_list[max_index+1:]))
        next_max_number = bank_list[next_max_index]
        return int(str(max_number) + str(next_max_number))

for line in data:
    joltage = process_bank_p1(line)
    total_1 += joltage

print("Total part 1: ", total_1)

# Part 2

def process_bank_p2(bank : str) -> int :
    joltage = ''
    number_to_add = 12
    last_index_used = 0
    bank_list = [int(x) for x in bank.strip()]

    for i in range(number_to_add, 0, -1) :
        # Remove i - 1 last elements and start at last_index_used
        tmp_bank_list = bank_list[last_index_used:-i+1] if i > 1 else bank_list[last_index_used:]
        max_index = tmp_bank_list.index(max(tmp_bank_list)) + last_index_used
        joltage += str(bank_list[max_index])
        bank_list[max_index] = 0
        last_index_used = max_index + 1
    
    return int(joltage)

for line in data:
    joltage = process_bank_p2(line)
    total_2 += joltage

print("Total part 2: ", total_2)