# Source: https://leetcode.com/problems/length-of-last-word/description/
# Author: Paulo Lemus
# Date  : 2017-11-11
# Info  : #58, Easy

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            return len(s.split()[-1])
        except:
            return 0

