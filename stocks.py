def max_profit(prices: list[int]) -> int:
    profit = []
    while prices != []:
        buy = min(prices)
        x = prices.index(buy)
        potential = prices[x:]
        sell = max(potential)
        profit.append(sell - buy)
        prices.remove(buy)
    print(profit)
    return max(profit)


def max_profit_optimized(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


max_profit_optimized(prices=[7, 1, 5, 3, 6, 4])
