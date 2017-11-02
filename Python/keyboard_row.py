# Source: https://leetcode.com/problems/keyboard-row/description/
# Author: Paulo Lemus
# Date  : 2017-11-01

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        mid = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        bot = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        one_liners = []

        for word in words:
            s = set(word.lower())
            if s.issubset(top) or s.issubset(mid) or s.issubset(bot):
                one_liners.append(word)

        return one_liners

