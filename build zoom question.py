def rounding_num(num):
    return int(num) if num % 1 < 0.5 else int(num) + 1

def solution(prices):
    total_price = rounding_num(sum(prices))
    price_dict = {(prices[i] % 1): int(prices[i]) for i in range(len(prices))}
    total_price_floored = sum(price_dict.values())
    difference = total_price - total_price_floored
    sorted_decimals = sorted(price_dict.keys())
    rounded_prices = []
    
    for i in range(len(sorted_decimals) - 1, -1, -1):
        if difference > 0:
            rounded_prices.append(int(price_dict[sorted_decimals[i]]) + 1)
            difference -= 1
        else:
            rounded_prices.append(int(price_dict[sorted_decimals[i]]))
    
    return rounded_prices
