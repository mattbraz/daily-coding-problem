"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def solve(superset):
    ret = set()
    def _solve(subset):
        ret.add(frozenset(subset))
        for e in subset:
            c = subset.copy()
            c.remove(e)
            _solve(c)
    _solve(superset)
    return ret


fs = frozenset
assert solve({1}) == {fs(), fs({1})}
assert solve({1,2}) == {fs(), fs({1}), fs({2}), fs({1, 2})}
assert solve({1,2,3}) == {fs(), fs({1}), fs({2}), fs({3}), fs({1, 2}), fs({1, 3}), fs({2, 3}), fs({1, 2, 3})}
assert solve(set()) == {fs()}

