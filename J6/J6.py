import numpy as np
import re

total_1 = 0
total_2 = 0
__path__ = './J6/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
transformed_lines = list(map(list, zip(*data)))
print(transformed_lines[-3:])

n1 = re.sub(' +', ' ', data[0]).split(' ')
n2 = re.sub(' +', ' ', data[1]).split(' ')
n3 = re.sub(' +', ' ', data[2]).split(' ')
n4 = re.sub(' +', ' ', data[3]).split(' ')
sign = re.sub(' +', ' ', data[4]).split(' ')
sign.remove('')

print(len(n1), len(n2), len(n3), len(n4), len(sign))
assert len(n1) == len(n2) == len(n3) == len(n4) == len(sign)

# Part 1
for i in range(len(n1)):
    if sign[i] =="+" :
        total_1 += int(n1[i]) + int(n2[i]) + int(n3[i]) + int(n4[i])
    else:
        total_1 += int(n1[i]) * int(n2[i]) * int(n3[i]) * int(n4[i])

print("Total part 1: ", total_1)

# Part 2

tmp = []
for col in transformed_lines :
    if col != [' ', ' ', ' ', ' ', ' '] :
        tmp.append(col)
    elif col == [' ', ' ', ' ', ' ', ' '] and len(tmp) > 0 :
        sign = tmp[0][4]
        tmp_total = 0
        for i in range(len(tmp)) :
            number = int((tmp[i][0] + tmp[i][1] + tmp[i][2] + tmp[i][3]).strip())
            if sign =="+" :
                tmp_total += number
            else:
                if i == 0 :
                    tmp_total = number
                else :
                    tmp_total *= number
        total_2 += tmp_total
        tmp = []
# To account for the last group if there's no trailing empty column
if len(tmp) > 0 :
    sign = tmp[0][4]
    tmp_total = 0
    for i in range(len(tmp)) :
        number = int((tmp[i][0] + tmp[i][1] + tmp[i][2] + tmp[i][3]).strip())
        if sign =="+" :
            tmp_total += number
        else:
            if i == 0 :
                tmp_total = number
            else :
                tmp_total *= number
    total_2 += tmp_total

print("Total part 2: ", total_2)