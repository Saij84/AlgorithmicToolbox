# Uses python3

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


def calc_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    idx1 = 0
    idx2 = 1
    result = idx1 + idx2

    i = 2

    while i < n+1:
        if i == 2:
            result = idx1 + idx2
        elif i == 3:
            result = idx2 + result
        else:
            idx1, idx2 = idx2, result
            result = (idx1 + idx2)
        i += 1
    return result


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    #if n > 60:

    for _ in range((n)-1):
        previous, current = current, previous + current
        sum += current
    return sum % 10

if __name__ == '__main__':
    input = "10000"
    n = int(input)

    print(fibonacci_sum_naive(n))
    print(calc_fib(n))

    if calc_fib(n) % 10 == fibonacci_sum_naive(n):
        print("OK")
    #print(fibonacci_sum_naive(n))
