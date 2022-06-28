"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None: return "nil"
    s1 = serialize(root.left)
    s2 = serialize(root.right)
    return ",".join([str(root.val), s1, s2])

def deserialize(s):
    elems = s.split(",")
    def _des():
        e = elems.pop(0)
        if e == 'nil': return None
        n = TreeNode(e)
        n.left = _des()
        n.right = _des()
        return n
    return _des()


tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(6))))
assert serialize(tree) == "1,2,nil,nil,3,4,5,nil,nil,6,nil,nil,nil"
assert deserialize(serialize(tree)).right.left.left.val == "5"

node = TreeNode('root', TreeNode('left', TreeNode('left.left')), TreeNode('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

