from math import inf

def DPChange(money, coins):
    min_num_coins = dict()
    min_num_coins[0] = 0

    for m in range(1, money + 1):
        min_num_coins[m] = inf
        for i in coins:
            if m >= i:
                print("min_num_coins[m - i] + 1 < min_num_coins[m]")
                print("-"*50)
                print("min_num_coins[m - i]+1:",  (m, i), min_num_coins[m - i]+1)
                print("min_num_coins[m]:", (m), min_num_coins[m])
                print(min_num_coins[m - i] + 1 < min_num_coins[m])
                print("\n")

                if min_num_coins[m - i] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - i] + 1
    return min_num_coins[money]

coins = [1, 5, 10]
money = 12
print(DPChange(money, coins))