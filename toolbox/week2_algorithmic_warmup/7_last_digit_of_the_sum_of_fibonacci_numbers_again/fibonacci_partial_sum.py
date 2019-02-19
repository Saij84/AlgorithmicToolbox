# Uses python3
import time

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next
        print(i, sum**2%10)

    return sum**2 % 10


def fibonacci_partial_sum_fast(from_, to):
    sum = 0

    current = 0
    next  = 1

    seq_len = (to - from_) % 60 #find len of the sequence

    from_ = from_ % 60 #instead of starting at 423521, start from 423521 % 60 which will keep the sequence small

    for i in range(from_+seq_len + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next
        print(i, sum**2 % 10)

    return sum**2 % 10


if __name__ == '__main__':
    input = "0 100"
    from_, to = map(int, input.split())

    t0 = time.time()
    print(fibonacci_partial_sum_naive(from_, to))
    t1 = time.time()
    print("time slow: {}".format(t1-t0))

    t0 = time.time()
    print(fibonacci_partial_sum_fast(from_, to))
    t1 = time.time()
    print("time slow: {}".format(t1 - t0))