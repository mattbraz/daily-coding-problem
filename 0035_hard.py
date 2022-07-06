"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def swap(a, i ,j): 
    a[i], a[j] = a[j], a[i]

def solve(arr):
    idx, ridx, bidx = 0, 0, len(arr)-1
    while idx <= bidx:
        if arr[idx] == 'G':
            idx += 1
        elif arr[idx] == 'B':
            swap(arr, idx, bidx)
            bidx -= 1
        elif arr[idx] == 'R':
            swap(arr, idx, ridx)
            ridx += 1
            idx += 1
    return arr


assert solve([]) == []
assert solve(['G']) == ['G']
assert solve(['B', 'G', 'R']) == ['R', 'G', 'B']
assert solve(['G', 'G', 'B', 'B', 'B', 'G']) == ['G', 'G', 'G', 'B', 'B', 'B']
assert solve(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']

