# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    maxVal = max(a, b)
    minVal = min(a, b)

    if b != 0:
        remainder = maxVal % minVal
        return gcd_fast(minVal, remainder)

    return maxVal



if __name__ == "__main__":
    input = "6 8"
    a, b = map(int, input.split())
    #print(gcd_naive(a, b))
    print(gcd_fast(a, b))