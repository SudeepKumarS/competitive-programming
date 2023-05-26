# You are given an array of prices where prices[i] is the price of a
# given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that
# stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0


from time_finder import calculate_execution_time


@calculate_execution_time
def max_profit_of_rates(rates: list) -> int:
    """
    To find the maximum profit of the given stock rates
    """
    max_profit = 0
    min_rate = rates[0]
    for rate in rates[1:]:
        min_rate = min(rate, min_rate)
        max_profit = max(max_profit, rate - min_rate)

    return max_profit


print(max_profit_of_rates([7,1,5,3,6,4]))
