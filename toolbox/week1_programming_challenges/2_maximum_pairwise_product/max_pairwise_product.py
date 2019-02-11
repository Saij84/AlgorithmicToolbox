# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 1
    index2 = 1

    for i in range(1, n):
        if numbers[i] > numbers[0]:
            index1 = numbers[i]

    if index1 == 1:
        index2 = 2
    else:
        index2 = 1

    for i in range(1, n):
        if numbers[i] != index1 and numbers[i] > index2:
            index2 = numbers[i]

    return index1*index2


if __name__ == '__main__':
    input_var = [5,6,2,7,4,9]
    #input_n = int(input_var)
    input_numbers = [int(x) for x in input_var]
    print(max_pairwise_product(input_numbers))
