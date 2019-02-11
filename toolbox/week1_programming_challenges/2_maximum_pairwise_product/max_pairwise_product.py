# python3
import random as rd


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
        index1 = numbers[0]
        index2 = numbers[1]

        for i in range(1, n):
            if numbers[i] > numbers[0]:
                index1 = numbers[i]

        for i in range(1, n):
            if numbers[i] != index1 and numbers[i] > index2:
                index2 = numbers[i]
        return index1 * index2
    else:
        return numbers[0] * numbers[1]

def stress_test(N, M):
    n = rd.randint(2, N)
    A = [rd.randint(0, M+1) for i in range(1, n+1)]

    print(A)

    if max_pairwise_product(A) == max_pairwise_product_naive(A):
        print("OK")
    else:
        print( max_pairwise_product(A), " is not equal to ", max_pairwise_product_naive(A))

if __name__ == '__main__':
    count = 0
    for i in range(100):
        N = rd.randint(1, 100)
        M = rd.randint(1, 1000)
        input_var = stress_test(10, 100000)