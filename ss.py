import random

def possible_combination(numbers, target):
    if target < 0:
        return False, []

    if target == 0:
        return True, []

    if len(numbers) == 0:
        return False, []

    for i in range(len(numbers)):
        possible_without_i, combination_without_i = possible_combination(numbers[i+1:], target)
        possible_with_i, combination_with_i = possible_combination(numbers[i+1:], target - numbers[i])

        if possible_without_i:
            return True, combination_without_i
        if possible_with_i:
            return True, [numbers[i]] + combination_with_i

    return False, []

seed = 42
random.seed(seed)

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)
target = 99
possible, combination = possible_combination(numbers, target)

print(possible)
print(combination)