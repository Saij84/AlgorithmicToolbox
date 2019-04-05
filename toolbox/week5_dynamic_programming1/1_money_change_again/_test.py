def recursive_change(money, coins):
    if money == 0:
        return 0
    min_num_coins = 0

    for i in range(len(coins)):
        if money >= coins[i]:
            num_coins = recursive_change(money - coins[i], coins)
            print(num_coins)
            if num_coins + 1 < min_num_coins:
                min_num_coins = num_coins + 1
                print(min_num_coins)
    return min_num_coins


def dp_change(money, coins):
    min_num_coins = 0

    for m in range(1, money):
        min_num_coins = m
        for i in range(1, len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coins[m - coins[i]] + 1
                if num_coins < min_num_coins:
                    min_num_coins = num_coins
    return min_num_coins


# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            if i - S[j] >= 0:
                x = table[i - S[j]][j]
            else:
                x = 0

            # Count of solutions excluding S[j]
            if j >= 1:
                y = table[i][j - 1]
            else:
                y = 0


            # total count
            table[i][j] = x + y
        print(table)
    return table[n][m - 1]


# Driver program to test above function
denom = [1, 5, 10]
coin_len = len(denom)
val = 10
print(count(denom, coin_len, val))

# This code is contributed by Bhavya Jain


#print(dp_change(10, [1, 5, 10, 20, 50]))
