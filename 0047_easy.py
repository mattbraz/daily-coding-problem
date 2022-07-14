"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def solve(prices):
    if len(prices) < 2: return None
    max_profit = 0
    max_price = prices.pop()
    for price in reversed(prices):
        max_profit = max(max_price - price, max_profit)
        max_price = max(price, max_price)
    return max_profit

assert solve([9, 11, 8, 5, 7, 10]) == 5
assert solve([9, 1, 8, 5, 17, 10]) == 16
assert solve([9, 20, 2, 5, 17, 10]) == 15
assert solve([10]) == None
assert solve([]) == None
