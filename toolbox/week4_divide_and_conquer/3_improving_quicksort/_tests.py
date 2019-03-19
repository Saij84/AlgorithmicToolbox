from toolbox.test_utils import test_utils as testU
from time import time
from sys import setrecursionlimit


setrecursionlimit(10**8)


@testU.function_timer
def selection_sort(arr):
    array_len = len(arr)

    for i in range(array_len):
        for j in range(i+1, array_len):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

@testU.function_timer
def merge_sorting(arr):
    array_len = len(arr)

    if array_len == 1:
        return arr



@testU.function_timer
def count_sort(arr):
    count = []
    array_len = len(arr)

    for i in range(array_len):
        count += 1



for i in range(1):
    rand_data = testU.array_generator(1, 1000, 1, 0)
    #print(rand_data)
    t1 = time()
    print(find_largest(rand_data, 0, 1000-1), "\n")
    t2 = time()

    print(t2-t1)