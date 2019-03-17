"""
test utils
"""
import random

# generate an array random or otherwise
def array_generator(start, end, isRandom=True, isRandomRange=False):
    if isRandom == True:
        if isRandomRange == True:
            end = random.randint(1, end)
        return [random.randint(start, end+1) for num in range(start, end+1)]
    else:
        return [num for num in range(start, end)]


