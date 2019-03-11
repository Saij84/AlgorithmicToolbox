def binary_search(a, low, high, key):
    if high < low:
        return low-1

    mid = low + (high-low)//2

    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid-1,  key)
    else:
        return binary_search(a, low, mid+1, key)