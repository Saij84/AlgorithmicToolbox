# Uses python3
import sys

# go through an array of none negative numbers, return majority number, else return number
def get_candidate(arr):
    counter, candidate = 0, None  # initialise variables
    for num in arr:
        if counter == 0:
            candidate, counter = num, 1  # new var assignment if counter is 0
        elif num == candidate:
            counter += 1
        else:
            counter -= 1
    return candidate

# check if the number return from get candidate is an majority number
def get_majority_element(arr):
    count, candidate = 0, get_candidate(arr)
    for i in arr:
        if i == candidate:
            count += 1

    if count > len(arr)/2:  # if the count is more than 50% of the total array
        return count
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *arr = list(map(int, input.split()))
    result = get_majority_element(arr)
    if result != -1:
        print(result, 1)
    else:
        print(0)
