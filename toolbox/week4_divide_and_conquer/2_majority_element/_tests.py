import random

def majorityElementNaive(a):
    array_size = len(a)

    for i in range(array_size):
        currentElement = a[i]
        count = 0

        for j in range(array_size):
            if a[j] == currentElement:
                count += 1
        if count > array_size/2:
            return 1
    return -1

def quickSearch(a):
    randNum = random.randint(0, len(a)-1)
    print("randNum", a[randNum])
    left = []
    right = []

    for i in range(len(a)):
        if a[i] <= a[randNum]:
            left.append(a[i])
        else:
            right.append(a[i])

    print(left, right)

def findCandidate(A):
    maj_index = 0
    count = 1

    for i in range(len(A)):
        #print("i:", i, "val:", A[i], "count:", count, "maj_index:", maj_index)
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        print("count:", count, i)
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index], count

def majority_element(arr):
    counter, possible_element = 0, None
    for i in arr:
        if counter == 0:
            possible_element, counter = i, 1
        elif i == possible_element:
            counter += 1
        else:
            counter -= 1

    return possible_element

rand_range = random.randint(1, 10)
data_in = [random.randint(1, rand_range) for i in range(1, rand_range)]


#data_in = [[2, 3, 9, 2, 2], [1, 5, 3, 4], [2, 1, 3, 1]]
print(data_in)
print(majority_element(data_in))
for a in data_in:
    pass
    #print(majorityElementNaive(a))
