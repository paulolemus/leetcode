# Source: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #345, Easy, 122 ms, 70.59%

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".


from collections import OrderedDict

class Solution:
    # 122 ms, 70.59%
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set('aeiouAEIOU')
        pairs = OrderedDict()

        # Get index and letter of all vowels
        for i, letter in enumerate(s):
            if letter in vowels:
                pairs[i] = letter

        # Invert the order of the vowels
        vowels = list(reversed(pairs.values()))
        for i, str_idx in enumerate(pairs):
            pairs[str_idx] = vowels[i]

        # Reconstruct and return string
        return ''.join([
            pairs[i] if i in pairs else letter for i, letter in enumerate(s)
        ])

