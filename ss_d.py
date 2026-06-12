import random
import numpy as np

def possible_combination(numbers, target):
    table = np.zeros((len(numbers), target + 1))
    table[:,0] = 1
    for i in range(len(numbers)):
        for j in range(1, target+1):
            remaining = j - numbers[i]
            table[i,j] = table[i-1,j] or (remaining >=0 and table[i-1,remaining])

    return bool(table[-1,-1]),table

def trace_combo(numbers,table):
    target = table.shape[1]-1
    if target == 0:
        return []
    last_number_index = table.shape[0]-1
    last_number = numbers[last_number_index]
    remaining = target - last_number
    if remaining >= 0 and table[-2, remaining]:
        return trace_combo(numbers,table[0:-1, 0:remaining+1])+[last_number]
    else:
        return trace_combo(numbers,table[0:-1, 0:target+1])

seed = 42
random.seed(seed)

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)
target = 99
possible, combination = possible_combination(numbers, target)

print(possible)

print(trace_combo(numbers,combination))