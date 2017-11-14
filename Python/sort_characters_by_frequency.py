# Source: https://leetcode.com/problems/sort-characters-by-frequency/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #451, Medium

# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


from collections import Counter

class Solution:
    # 272 ms, 6.45%
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)
        return ''.join(sorted(s, key=lambda ch: (counts[ch], ch), reverse=True))

