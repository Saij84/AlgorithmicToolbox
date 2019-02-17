# Uses python3
import time

def get_pisano_period(m):
    val1 = 0
    val2 = 1

    seq_len = 0
    while seq_len < m*m:
        remainder = (val1 + val2) % m
        val1 = val2
        val2 = remainder
        seq_len += 1

        if val1 == 0 and val2 == 1:
            return seq_len


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    remainder = n % get_pisano_period(m)

    for _ in range(remainder-1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


if __name__ == '__main__':
    input = "8374293856215619875 10"
    n, m = map(int, input.split())

    # t0 = time.time()
    # print(fibonacci_sum_naive(n))
    # t1 = time.time()
    # print("Slow time: {}".format(t1-t0))

    t0 = time.time()
    print (fibonacci_sum_fast(n, m))
    t1 = time.time()
    print("fast time: {}".format(t1 - t0))

"""
00 01 02 03 04 05 06 07 08 09 
00 01 01 02 03 05 08 13 21 34
00 01 02 04 07 13 21 34 55 89
"""