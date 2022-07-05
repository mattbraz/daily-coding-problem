"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

def solve(string):
    stack = []
    for char in string:
        if char in pairs.values():
            stack.append(char) 
        elif char in pairs.keys():
            if stack.pop() != pairs[char]:
                return False
    return not stack


assert solve("([])[]({})") == True
assert solve("([{}[[]()]])[]({[][]})") == True
assert solve("([)]") == False
assert solve("((()") == False
assert solve("(234)") == True
assert solve("") == True

