# Source: https://leetcode.com/problems/word-pattern/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #290, Easy, 69 ms, 22.58%


class Solution:
    # 69 ms, 22.58%
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        matcher = {}
        used_words = set()

        if len(pattern) != len(words):
            return False

        for idx, letter in enumerate(pattern):
            word = words[idx]
            if letter not in matcher and word not in used_words:
                matcher[letter] = word
                used_words.add(word)
            if word != matcher.get(letter):
                return False
        return True

