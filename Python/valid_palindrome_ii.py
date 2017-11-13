# Source: https://leetcode.com/problems/valid-palindrome-ii/description/
# Author: Paulo Lemus
# Date  : 2017-12-13
# Info  : #680, Easy

# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.subPalindrome(s, 0, len(s)-1, False)

    def subPalindrome(self, s, head, tail, skipped):
        mid = (head + tail) // 2

        while head <= mid and tail >= mid:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            elif not skipped:
                isPalindrome  = self.subPalindrome(s, head+1, tail, True)
                isPalindrome |= self.subPalindrome(s, head, tail-1, True)
                return isPalindrome
            else:
                return False

        return True

