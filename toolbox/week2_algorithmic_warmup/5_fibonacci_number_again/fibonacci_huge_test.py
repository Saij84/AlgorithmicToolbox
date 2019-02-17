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

def get_fibonacci_huge(n, m):
    get_len = get_pisano_period(m)

    remainder = n % get_len

    first = 0
    second = 1
    res = remainder

    i = 1
    while i < remainder:
        res = (first + second) % m
        first = second
        second = res
        i += 1

    return res % m


t0 = time.time()
print(get_fibonacci_huge(5, 10))
t1 = time.time()

print(t1-t0)