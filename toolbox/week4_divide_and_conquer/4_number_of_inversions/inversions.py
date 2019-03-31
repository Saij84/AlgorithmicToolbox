# Uses python3
import sys
from utils.src.array_utils import array_utils as aUtils

"""
[4, 10, 8, 7, 0, 2, 8, 10] input array

left [4] right [10]
result: [4]
result: [4, 10]


left [8] right [7]
result: [7]
result: [7, 8]


left [4, 10] right [7, 8]
result: [4]
result: [4, 7]
result: [4, 7, 8]
result: [4, 7, 8, 10]


left [0] right [2]
result: [0]
result: [0, 2]


left [8] right [10]
result: [8]
result: [8, 10]


left [0, 2] right [8, 10]
result: [0]
result: [0, 2]
result: [0, 2, 8]
result: [0, 2, 8, 10]


left [4, 7, 8, 10] right [0, 2, 8, 10]
result: [0]
result: [0, 2]
result: [0, 2, 4]
result: [0, 2, 4, 7]
result: [0, 2, 4, 7, 8]
result: [0, 2, 4, 7, 8, 8]
result: [0, 2, 4, 7, 8, 8, 10]
result: [0, 2, 4, 7, 8, 8, 10, 10]


[0, 2, 4, 7, 8, 8, 10, 10]
"""

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions

    ave = (left + right) // 2

    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    print(merge(a, b, left, ave, right))

    #write your code here
    return number_of_inversions

def merge(arr, b, left, mid, right):
    """
    Merging function for merge sort

    :param left: array
    :param right: array
    :return: sorted array
    """

    i, j, k = left, mid, left

    result = []
    count = 0

    while i <= mid-1 and j <= right:
        print(i, j, k, mid)
        if arr[i] <= arr[j]:  # run when there are items in both lef and right arrays
            b[k] = arr[i]
            k += 1
            i += 1
        else:
            b[k] = arr[j]
            k += 1
            j += 1
            count += 1
        print("b", b, i, j, k, count)
    while(i <= mid-1):
        b[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        b[k] = arr[j]
        k += 1
        j += 1

    # for i in range(left, right):
    #     arr[i] = b[i]

    print(count)
    print("\n")

    return result


if __name__ == '__main__':
    for i in range(1):
        in_data = [2,3,9,2,9]  # aUtils.array_generator(0, 10, arr_size=8, isRandomRange=False)
        input = in_data
        n, a = len(input), input
        b = n * [0]
        print(in_data)
        print(get_number_of_inversions(a, b, 0, len(a)))
