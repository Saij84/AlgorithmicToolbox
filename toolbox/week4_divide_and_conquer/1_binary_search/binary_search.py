# Uses python3
import sys
sys.setrecursionlimit(10**5)
import time

def binary_search(a, key):
    # write your code here
    left, right = 0, len(a) - 1

    if key > a[right-1]:  # check if key is lager than the largest number
        return -1

    mid = left + (right - left) // 2  # find mid

    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a[:mid-1], key)
    else:
        return (mid+1) + binary_search(a[mid+1:], key)

def linear_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]

    for key in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print((binary_search(a, key)), end = ' ')

