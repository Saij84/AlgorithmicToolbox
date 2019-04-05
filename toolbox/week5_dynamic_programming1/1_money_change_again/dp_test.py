from utils.src.array_utils import array_utils as aUtils

def min_coins(val, denom, coin_len):
    tables = []
    # table2 = [for i in range(coin_len) if i>1 [0 for x in range(val+1)]  ]

    for i in range(coin_len):
        if i < 1:
            tables.append([i for i in range(val+1)])
        else:
            tables.append([0 for i in range(val+1)])



    print(tables)


# Driver program to test above function
denom = [1, 5, 10]
coin_len = len(denom)
val = 10
print(min_coins(val, denom, coin_len))