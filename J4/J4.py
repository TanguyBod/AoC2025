import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J4/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
        
# Part 1

nb_rows = len(data)
nb_cols = len(data[0])
data_array = np.array([[1 if char == '@' else 0 for char in line.strip()] for line in data])

def is_accessible(array: np.ndarray, row: int, col: int) -> bool:
    total = 0
    # Check all 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < nb_rows and 0 <= c < nb_cols:
            total += array[r, c]

    if total < 4 :
        return True
    return False

for r in range(nb_rows):
    for c in range(nb_cols):
        if data_array[r, c] == 1 and is_accessible(data_array, r, c):
            total_1 += 1


print("Total part 1: ", total_1)

# Part 2

def nb_removable (array: np.ndarray, row: int, col: int) :
    total = 0
    modified_array = array.copy()
    for r in range(nb_rows):
        for c in range(nb_cols):
            if data_array[r, c] == 1 and is_accessible(data_array, r, c):
                total += 1
                modified_array[r, c] = 0

    return total, modified_array

while True :
    removable, data_array = nb_removable(data_array, r, c)
    if removable == 0 :
        break
    total_2 += removable

print("Total part 2: ", total_2)