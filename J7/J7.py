import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J7/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
input_array = np.array(list(map(list, zip(*data))))
input_array_part2 = input_array.copy()
# input_array : X -> rows, Y -> columns

# Part 1
for j in range(1, input_array.shape[1]) :
    for i in range(input_array.shape[0]) :
        if input_array[i][j-1] == "S" :
            input_array[i][j] = "|"
        elif input_array[i][j-1] == "|" :
            if input_array[i][j] == "." :
                input_array[i][j] = "|"
            elif input_array[i][j] == "^" :
                input_array[i-1][j] = "|"
                input_array[i+1][j] = "|"
                total_1 += 1
print("Total part 1: ", total_1)

# Part 2
weight_array = np.zeros(input_array_part2.shape, dtype=int)
weight_array[input_array_part2 == "S"] = 1
weight_array[input_array_part2 == "^"] = -1

for j in range(1, weight_array.shape[1]) :
    for i in range(weight_array.shape[0]) :
        if weight_array[i][j-1] >= 0 : # If the previous cell has a weight of 0 or more
            if weight_array[i][j] == 0 :
                weight_array[i][j] = weight_array[i][j-1]
            elif weight_array[i][j] == -1 :
                weight_array[i-1][j] += weight_array[i][j-1]
                if weight_array[i+1][j-1] >= 0 :
                    weight_array[i+1][j] += weight_array[i][j-1] + weight_array[i+1][j-1]
                else :
                    weight_array[i+1][j] += weight_array[i][j-1]
            
for i in range(weight_array.shape[0]) :
    if weight_array[i][-1] > 0 :
        total_2 += weight_array[i][-1]

print("Total part 2: ", total_2)