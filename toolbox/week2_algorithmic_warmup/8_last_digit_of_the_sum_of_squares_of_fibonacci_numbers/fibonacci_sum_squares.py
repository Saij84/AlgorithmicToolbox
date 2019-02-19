# Uses python3
import time

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for i in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_fast(n):
    seq_len = n % 60

    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for i in range(seq_len - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = 7

    t0 = time.time()
    sumFast = fibonacci_sum_squares_fast(n)
    t1 = time.time()
    print(sumFast)
    print("time slow: {}".format(t1 - t0))

    # if sumNaive == sumFast:
    #     print("OK!")