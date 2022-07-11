"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""


def solve(flights, start):
    def _solve(cur, available, visited):
        if not available and flights:
            return [start] + [v[1] for v in visited]
        for pair in sorted([a for a in available if a[0] == cur]):
            if partial := _solve(pair[1], available - {pair}, visited + [pair]):
                return partial
        return None
    return _solve(start, set(flights), [])


flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
assert solve(flights, 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

flights = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
assert solve(flights, 'A') == ['A', 'B', 'C', 'A', 'C']

flights = [('a','d'), ('a','c'), ('a','b'), ('d','a'), ('c','a'), ('b','a')]
assert solve(flights, 'a') == ['a','b','a','c','a','d','a']

flights = [('A', 'B'), ('A', 'C'), ('D', 'A')]
assert solve(flights, 'A') is None

flights = []
assert solve(flights, 'A') is None

