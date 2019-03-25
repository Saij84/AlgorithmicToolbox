# Uses python3
import sys
import random
from utils.src.array_utils import array_utils as aUtils


def partition3_1(a, l, r):
    pivot, l_idx, r_idx = a[l], l, r
    idx = l_idx

    while idx <= r_idx:
        if a[idx] < pivot:
            a[l_idx], a[idx] = a[idx], a[l_idx]
            l_idx += 1

        elif a[idx] > pivot:
            a[r_idx], a[idx] = a[idx], a[r_idx]
            r_idx -= 1
            idx -= 1
        idx += 1
    return l_idx, r_idx


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



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    m3, m4 = partition3_1(a, l, r)
    print("orig:", m1, m2)
    print(" new:", m3, m4)


    #
    # randomized_quick_sort(a, l, m1)
    # randomized_quick_sort(a, m2 + 1, r)
    # return a


if __name__ == '__main__':
    input = [8, 9, 4, 6, 7, 10, 6, 7, 4, 4]  # aUtils.array_generator(1, 10, arr_size=10, isRandomRange=False)
    n, a = len(input), input
    print(input)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
