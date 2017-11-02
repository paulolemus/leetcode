# Source: https://leetcode.com/problems/single-number/description/
# Author: Paulo Lemus
# Date  : 2017-11-01

# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set()

        for num in nums:
            if num in numset:
                numset.remove(num)
            else:
                numset.add(num)
        return numset.pop()



    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singleton = 0

        for num in nums:
            singleton ^= num
        return singleton
