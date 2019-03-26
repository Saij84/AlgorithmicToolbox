# Uses python3
import sys
import random
from utils.src.array_utils import array_utils as aUtils
from utils.src.checking_utils import checking_utils as cUtils


def partition3(a, l, r):
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

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)

    randomized_quick_sort(a, l, m1)
    randomized_quick_sort(a, m2 + 1, r)
    return a


if __name__ == '__main__':
    for i in range(10):
        input = aUtils.array_generator(1, 500, arr_size=25, isRandomRange=True)
        n, a = len(input), input
        print(input)
        result = randomized_quick_sort(a, 0, n - 1)
        print(cUtils.growing_num(result))
        for x in a:
            print(x, end=' ')
        print("\n")
