from random import randint as rdInt

n = 100

numArray = [rdInt(1, n) for i in range(n)]


def Range(list1):
    largest = list1[0]
    largest2 = list1[0]

    for item in list1:
        if item > largest:
            largest = item
        elif largest2 != largest and largest2 < item:
            largest2 = item


    print("Largest element is:", largest)
    print("Second Largest element is:", largest2)


Range(numArray)