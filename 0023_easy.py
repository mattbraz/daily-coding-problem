"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. 
You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

def solve(matrix, start, end):
    def _solve(cur, visited):
        if cur[0] < 0 or cur[1] < 0:
            return None
        if cur[0] >= len(matrix) or cur[1] >= len(matrix[0]):
            return None
        if matrix[cur[0]][cur[1]]:
            return None
        if cur in visited:
            return None
        if cur == end:
            return len(visited)

        steps = []
        steps.append(_solve((cur[0], cur[1]+1), visited + [cur]))
        steps.append(_solve((cur[0], cur[1]-1), visited + [cur]))
        steps.append(_solve((cur[0]+1, cur[1]), visited + [cur]))
        steps.append(_solve((cur[0]-1, cur[1]), visited + [cur]))
        valid = [x for x in steps if x is not None]
        return min(valid) if valid else None
    return _solve(start, [])


m = [[False, False, False, False],
     [True, True, False, True],
     [False, False, False, False],
     [False, False, False, False]]
assert solve(m, (3, 0), (0, 0)) == 7

m = [[False, False, False],
     [False, True, False]]
assert solve(m, (1, 0), (1, 2)) == 4

m = [[False, True, False],
     [False, True, False]]
assert solve(m, (1, 0), (1, 2)) is None

