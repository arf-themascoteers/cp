import random
import numpy as np

def possible_combination(numbers, target):
    np.zeros((len(numbers), target + 1))


seed = 42
random.seed(seed)

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)
target = 99
possible, combination = possible_combination(numbers, target)

print(possible)
print(combination)