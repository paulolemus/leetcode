# Source: https://leetcode.com/problems/valid-parentheses/description/
# Author: Paulo Lemus
# Date  : 2017-11-18
# Info  : #20, Easy, 49 ms, 92.97%

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


# 49 ms, 92.97%
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        try:
            for letter in s:
                if letter in matching:
                    stack.append(matching[letter])
                elif letter == stack[-1]:
                    stack.pop()
                else:
                    return False
        except:
            return False

        return len(stack) == 0

