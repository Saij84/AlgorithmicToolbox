from utils.src.array_utils import array_utils as aUtils
from utils.src.time_utils import time_utils as tUtils

@tUtils.function_timer
def selection_sort(arr):
    array_len = len(arr)

    for i in range(array_len):
        for j in range(i+1, array_len):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr




def count_sort(arr):
    count = []
    array_len = len(arr)

    for i in range(array_len):
        count += 1

for i in range(1):
    data_in = aUtils.array_generator(1,9, isRandomRange=False)
    print(data_in)
    print(merge_sort(data_in))

