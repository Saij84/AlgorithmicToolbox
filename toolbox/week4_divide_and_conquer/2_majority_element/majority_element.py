# Uses python3
import sys

# go through an array of none negative numbers, return majority number, else return number
def get_candidate(arr):
    counter, possible_element = 0, None
    for i in arr:
        if counter == 0:
            possible_element, counter = i, 1
        elif i == possible_element:
            counter += 1
        else:
            counter -= 1
    return possible_element

# check if the number return from get candidate is an majority number
def get_majority_element(a):
    candidate = get_candidate(a)
    count = 0

    for i in a:
        if i == candidate:
            count += 1

    if count > len(a)/2:
        return count
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
