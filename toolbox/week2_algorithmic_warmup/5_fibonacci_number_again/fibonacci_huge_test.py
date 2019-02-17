import time

def get_pisano_period(m):
    a = 0
    b = 1

    i = 0
    while i < m * m:
        c = (a + b) % m
        a = b
        b = c
        i += 1
        if a == 0 and b == 1:
            return i

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
print(get_pisano_period(3))
print(get_fibonacci_huge(2816213588, 239))
t1 = time.time()

print(t1-t0)