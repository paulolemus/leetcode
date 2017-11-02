# Source: https://leetcode.com/problems/move-zeroes/description/
# Author: Paulo Lemus
# Date  : 2017-11-01

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        zero_idx = 0

        # Move to the first zero in the list
        while idx < len(nums) and nums[idx] != 0:
            idx += 1
        zero_idx = idx

        # Swap any numbers with earliest zero
        while idx < len(nums):
            if nums[idx] != 0:
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx]
                idx += 1
                zero_idx += 1
            else:
                idx += 1

