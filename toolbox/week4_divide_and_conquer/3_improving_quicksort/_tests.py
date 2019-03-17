from toolbox.test_utils import test_utils as testU

def swap(arr, src, trg):
    arr[trg], arr[src] = arr[src], arr[trg]
    return arr

@testU.function_time
def selection_sort(arr):
    array_len = len(arr)

    for i in range(array_len):
        for j in range(i+1, array_len):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

for i in range(10):
    rand_data = testU.array_generator(1, 50, 1, 1)
    print(selection_sort(rand_data), "\n")
