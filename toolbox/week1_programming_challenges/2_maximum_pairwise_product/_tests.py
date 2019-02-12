from random import randint as rdInt

n = 100

numArray = [rdInt(1, n) for i in range(n)]

print(numArray)

idx1 = numArray[0]
idx2 = numArray[1]

for i in range(2, n):
    if numArray[i] >= idx1:
        idx2 = idx1
        idx1 = numArray[i]
print(idx1, idx2)
print(idx1 * idx2)

