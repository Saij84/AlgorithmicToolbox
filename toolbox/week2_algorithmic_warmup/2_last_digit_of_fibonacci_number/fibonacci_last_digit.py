# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))

def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    idx1 = 0
    idx2 = 1
    result = 0

    i = 2

    while i < n+1:
        if i == 2:
            result = (idx1 + idx2)%10
        elif i == 3:
            result = idx2 + result
        else:
            idx1 = idx2
            idx2 = result
            result = (idx1 + idx2)%10
        i += 1
    return result
print(calc_fib(331))