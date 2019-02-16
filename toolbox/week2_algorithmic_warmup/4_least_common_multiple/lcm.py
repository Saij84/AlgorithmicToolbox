# Uses python3
import time

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    upperLimLCM = a*b

    maxVal = max(a, b)
    minVal = min(a, b)

    lcm = maxVal
    while lcm <= upperLimLCM:
        if lcm % maxVal == 0 and lcm % minVal == 0:
            return lcm
        else:
            lcm += maxVal
    return upperLimLCM


if __name__ == '__main__':
    input = "6002003 8200005"
    a, b = map(int, input.split())
    t0 = time.time()
    print(lcm_fast(a, b))
    t1 = time.time()
    print(t1 - t0)

    # t0 = time.time()
    # print(lcm_naive(a, b))
    # t1 = time.time()
    # print(t1 - t0)

