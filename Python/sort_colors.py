# Source: https://leetcode.com/problems/sort-colors/description/
# Author: Paulo Lemus
# Date  : 2017-11-02

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0

        for i, color in enumerate(nums):
            if color == 0:
                # Found red
                nums.insert(r, nums.pop(i))
                w += 1
                b += 1
            elif color == 1:
                # Found white
                nums.insert(w, nums.pop(i))
                b += 1
            else:
                nums.insert(b, nums.pop(i))

