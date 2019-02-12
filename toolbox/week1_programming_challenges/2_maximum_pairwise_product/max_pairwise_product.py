# python3
import random as rd
import timeit


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    a = [int(x) for x in numbers]
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, a[i] * a[j])
    return product


def max_pairwise_product(numbers):
    n = len(numbers)
    if n > 2:
        idx1 = numbers[0]
        idx2 = numbers[1]

        if idx1 < idx2:
            idx1 = numbers[1]
            idx2 = numbers[0]

        for i in range(2, n):
            if numbers[i] >= idx1:
                idx2 = idx1
                idx1 = numbers[i]
            elif numbers[i] > idx2 < idx1:
                idx2 = numbers[i]
        #print(idx1, idx2)
        return idx1*idx2
    elif n == 1:
        return 0
    else:
        return numbers[0] * numbers[1]

def stress_test(N, M):
    n = rd.randint(2, N)
    A = [rd.randint(0, M) for i in range(1, n)]

    print(A)

    if max_pairwise_product(A) == max_pairwise_product_naive(A):
        print("OK")
    else:
        print(max_pairwise_product(A), "is NOT equal to", max_pairwise_product_naive(A))

if __name__ == '__main__':
    count = 0
    for i in range(100):
        N = rd.randint(1, 100)
        M = rd.randint(1, 1000)
        input_var = stress_test(10, 100000)
