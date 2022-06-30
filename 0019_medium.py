"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

def solve(matrix, n=0, cost=0, prev_k=None):
        if n >= len(matrix): return cost
        costs = []
        for k in range(len(matrix[n])):
            if prev_k and k == prev_k: continue
            c = solve(matrix, n+1, cost + matrix[n][k], k)
            costs.append(c)
        return min(costs)

costs = [
    [1,2,2],
    [2,2,1],
    [2,1,2],
    [2,2,1],
    [5,5,1],
]
assert solve(costs) == 6

costs = [
    [7, 2, 5, 6, 9, 2, 4],
    [3, 8, 7, 2, 4, 3, 1],
    [9, 5, 4, 8, 7, 6, 1]
]
assert solve(costs) == 5
