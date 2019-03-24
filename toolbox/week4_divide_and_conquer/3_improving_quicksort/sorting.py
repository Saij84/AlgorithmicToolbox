# Uses python3
import sys
import random
from utils.src.array_utils import array_utils as aUtils


# def partition3(a, l, r):
#     k = a[0]
#     left_c = 0
#     mid_c = 0
#
#     if mid_c == len(a):
#         return
#
#     for i in range(1, len(a)):
#         if a[i] < k:
#             left_c += 1
#             a[i], a[left_c] = a[left_c], a[i]
#     a[l], a[left_c] = a[left_c], a[l]h9
#     mid_c = left_c
#
#     for i in range(left_c+1, len(a)):
#         if a[i] > k:
#             mid_c += 1
#             a[i], a[mid_c] = a[mid_c], a[i]
#     a[r], a[mid_c] = a[mid_c], a[r]
#
#     return left_c, mid_c

def partition3(a, l, r):
    x, j, t = a[l], l, r
    i = j

    while i <= t:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
        t -= 1
        i -= 1  # remain in the same i in this case
    i += 1
    return j, t


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    print(k, m1, m2)

    # m = partition2(a, l, r)

    randomized_quick_sort(a, l, m1)
    randomized_quick_sort(a, m2 + 1, r)
    return a


if __name__ == '__main__':
    input = [8, 9, 4, 6, 7, 10, 6, 7, 4, 4]  # aUtils.array_generator(1, 10, arr_size=10, isRandomRange=False)
    n, a = len(input), input
    print(input)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
