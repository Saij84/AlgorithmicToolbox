# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return n + calc_fib(n - 1)

n = int(input())
print(calc_fib(n))
