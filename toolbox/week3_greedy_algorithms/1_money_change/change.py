# Uses python3
import sys

def get_change(m):
    denominations = [10, 5, 1]

    change = 0

    for deno in denominations:

        remain = m//deno
        change += remain
        m = m - (remain*deno)
    return change

if __name__ == '__main__':
    m = int(28)
    print(get_change(m))
