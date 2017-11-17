# Source: https://leetcode.com/problems/contains-duplicate/description/
# Author: Paulo Lemus
# Date  : 2017-11-16
# Info  : #217, Easy, 68 ms, 87.76%

# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least
# twice in the array, and it should return false if every element
# is distinct.


# 68 ms, 87.76 %
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        nums.sort()

        last = nums[0]

        for i in range(1, len(nums)):
            if last != nums[i]:
                last = nums[i]
            else:
                return True
        return False

