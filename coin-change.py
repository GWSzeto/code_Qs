import sys
def coinChange(coins, amount):
    memo = [0]
    for sub_amount in range(1, amount + 1):
        min = sys.maxsize
        for coin in coins:
            rem  = sub_amount - coin
            if rem >= 0 and memo[rem] >= 0 and memo[rem] + 1 < min:
                min = memo[rem] + 1

        if min != sys.maxsize:
            memo.append(min)
        else:
            memo.append(-1)
        print(memo)

    return memo[amount]

print(coinChange([2], 3))
