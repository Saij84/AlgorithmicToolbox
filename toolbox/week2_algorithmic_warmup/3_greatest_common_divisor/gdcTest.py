# Uses python3
import sys

def gcd_fast(a, b):
    maxVal = max(a, b)
    minVal = min(a, b)

    if b != 0:
        remainder = maxVal % minVal
        return gcd_fast(minVal, remainder)

    return maxVal

print(gcd_fast(28851538, 1183019))