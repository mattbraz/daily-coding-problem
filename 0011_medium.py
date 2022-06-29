"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


class Trie:
    def __init__(self, words):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.terminal = True

    def get_words(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        ret = []
        def _foo(prefix, node):
            if node.terminal:
                ret.append(prefix)
            for char in node.children:
                _foo(prefix+char, node.children[char])
        _foo(prefix, node)
        return ret


class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.terminal = False


def solve(words, query):
    trie = Trie(words)
    for word in words:
        trie.add_word(word)
    return trie.get_words(query)


assert solve(['dog', 'deer', 'deal'], 'de') == ['deer', 'deal']
assert solve(['dog', 'deer', 'deal'], 'd') == ['dog', 'deer', 'deal']
assert solve(['dog', 'deer', 'deal', 'dealer'], 'dea') == ['deal', 'dealer']
assert solve(['arc', 'beer', 'crud', 'area'], 'a') == ['arc', 'area']
assert solve(['arc', 'beer', 'crud', ''], 'x') == []

