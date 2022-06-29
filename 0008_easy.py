"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def solve(root):
    def _solve(root):
        if not root.left and not root.right:
            return (1, root.val, True)  # count, value, is_unival
        if root.left:
            lc,lv,li = _solve(root.left)
        if root.right:
            rc,rv,ri = _solve(root.right)
        if li and ri and root.val == lv and root.val == rv:
            return (lc+rc+1, root.val, True)
        else:
            return (lc+rc, root.val, False)
    return _solve(root)[0]


r = TreeNode(0, TreeNode(1), TreeNode(0))
assert solve(r) == 2
r = TreeNode(1, TreeNode(1), TreeNode(1))
assert solve(r) == 3

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

r = TreeNode(0, TreeNode(1), TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0)))
assert solve(r) == 5

#   0
#  / \
# 1   1
#    / \
#   1   1
#  / \
# 1   0

r = TreeNode(0, TreeNode(1), TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(0)), TreeNode(1)))
assert solve(r) == 4

