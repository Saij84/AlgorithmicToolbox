


def stress_test(N, M):
    n = rd.randint(2, N)
    A = [rd.randint(0, M+1) for i in range(1, n+1)]

    return A

stress_test(10, 100)