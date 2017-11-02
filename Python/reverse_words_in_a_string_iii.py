# Source: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Author: Paulo Lemus
# Date  : 2017-11-01


# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


class Solution:
    def reverseWords(self, s):
	"""
	:type s: str
	:rtype: str
	"""
	words = s.split()
	for i, word in enumerate(words):
	    words[i] = word[::-1]

	return ' '.join(words)

