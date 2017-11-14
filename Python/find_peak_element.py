# Source: https://leetcode.com/problems/find-peak-element/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #162, Medium, 65 ms, 44.07%


# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# click to show spoilers.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


# 66 ms, 42.37%
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base case
        if len(nums) < 2:
            return 0

        # Edge cases
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1

        # General middle cases
        idx = 1
        while idx < len(nums)-1:
            if nums[idx-1] < nums[idx] > nums[idx+1]:
                return idx
            idx += 1

# 65 ms, 44.07%
class Solution2:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(float('-inf'))

        for i, num in enumerate(nums):
            if nums[i-1] < num > nums[i+1]:
                return i

