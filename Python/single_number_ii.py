# Source: https://leetcode.com/problems/single-number-ii/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #137, Medium, 56 ms, 91.30%

# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        for key in c:
            if c[key] == 1:
                return key

