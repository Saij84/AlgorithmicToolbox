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