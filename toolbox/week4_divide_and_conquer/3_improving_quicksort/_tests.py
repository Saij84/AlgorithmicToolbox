from toolbox.test_utils import test_utils as testU

def swap(arr, src, trg):
    src = arr[src]
    trg = arr[trg]
    swap = arr[trg]

    print(src, trg, swap)
    arr[src] = trg
    trg[trg] = swap

    return arr
def selection_sort(arr):
    array_len = len(arr)-1
    for i in range(array_len):
        min_index = i
        for j in range(i+1, array_len):
            if arr[i] < arr[min_index]:
                min_index = j



for i in range(30):
    rand_data = testU.array_generator(1, 10, 1, 1)
    print(rand_data)
# print(swap(rand_data, 0, 5))
