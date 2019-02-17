# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    count = 0
    for _ in range(n - 1):
        previous, current = current, previous + current

        print(current % m)
        count += 1
    return current % m

if __name__ == '__main__':
    input = " 239"
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
