# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k = n
    index = 1  # starting number

    while k > 0:  # run until k is equal to zero
        if k <= 2 * index:  # while k decrease and index increase, trigger when smaller or equal to
            summands.append(k)
            k -= k  # set k to zero
        else:
            summands.append(index)  # push index to back of summands list
            k -= index  # decrease k by index
        index += 1  # increase index by one
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
