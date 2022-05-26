"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# O(n)
def solve(k, nums):
    seen = set()
    for n in nums:
        if (k-n) in seen: return True
        else: seen.add(n)
    return False

# O(n^2)
def solve_slow(k, nums):
    if len(nums) == 0: return False
    n = nums.pop(0)
    for x in nums:
        if n + x == k: return True
    return solve(k, nums)



assert solve(17, []) == False
assert solve(17, [17]) == False
assert solve(17, [10, 15, 3, 7]) == True
assert solve(17, [5, 10, 15, 3, 7, 5]) == True
assert solve(17, [10, 15, 3, 8]) == False

