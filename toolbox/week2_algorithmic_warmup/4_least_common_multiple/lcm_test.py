# Uses python3

import time


def lcm_fast(a, b):
    upperLim = a*b

    maxVal = max(a, b)
    minVal = min(a, b)

    i = maxVal

    while i != upperLim:
        if i % maxVal == 0 and i % minVal == 0:
            return i
        else:
            i += maxVal
    return upperLim


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


if __name__ == '__main__':
    input = "3005 22726"
    a, b = map(int, input.split())

    t0 = time.time()
    print(lcm_test(a, b))
    t1 = time.time()
    print(t1 - t0)

    t0 = time.time()
    print(lcm_naive(a, b))
    t1 = time.time()
    print(t1 - t0)
