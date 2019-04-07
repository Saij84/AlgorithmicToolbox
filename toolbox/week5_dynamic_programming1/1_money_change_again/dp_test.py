from utils.src.array_utils import array_utils as aUtils
from utils.src.time_utils import time_utils as tUtils

@tUtils.function_timer
def create_valTables(val, denom, coin_len):
    tables = []
    # table2 = [for i in range(coin_len) if i>1 [0 for x in range(val+1)]  ]

    for i in range(coin_len):
        if i < 1:
            tables.append([i for i in range(val+1)])
        else:
            tables.append([0 for i in range(val+1)])

    for table_idx in range(1, len(tables)):
        for val in enumerate(tables[table_idx]):
            if val[0]/denom[table_idx] >= 1:
               tables[table_idx][val[0]] += 1
    return tables



def find_coins(val, denom, tables):
    coin_val = []

    if val == 0:
        return coin_val

    for i in enumerate(tables):
        if i[1][-1] != 0:
            val -= denom[i[0]]
    








# Driver program to test above function
denom = [1, 5, 10, 20, 50, 100]
coin_len = len(denom)
val = 12

val_tables = create_valTables(val, denom, coin_len)
print(find_coins(val, denom, val_tables))