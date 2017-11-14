# Source: https://leetcode.com/problems/search-insert-position/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #35, Easy, 65 ms, 50%

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2


# 65 ms, 50%
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

