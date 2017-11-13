# Source: https://leetcode.com/problems/longest-common-prefix/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #14, Easy, 55 ms, 93%

# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        letter_idx = 0
        try:
            while True:
                letter = strs[0][letter_idx]
                for s in strs:
                    if s[letter_idx] != letter:
                        raise Exception
                prefix.append(letter)
                letter_idx += 1
        except:
            pass
        return ''.join(prefix)

