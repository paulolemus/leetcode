# Source: https://leetcode.com/problems/valid-palindrome/description/
# Author: Paulo Lemus
# Date  : 2017-11-11
# Info  : #125, Easy

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([ch for ch in s if ch.isalnum()])
        s = s.lower()
        return s == s[::-1]

