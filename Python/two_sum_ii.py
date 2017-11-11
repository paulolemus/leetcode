# Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Author: Paulo Lemus
# Date  : 2017-11-10
# Info  : #167, Easy

# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such
# that they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2)
# are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Iterate the list, adding the target - nums[i] to a map, difference to index.
        # Once we reach an item that is a key in the map, return its index and the mapped index
        complements = {}

        for i, num in enumerate(numbers):
            if num in complements:
                return [complements[num] + 1, i + 1]
            else:
                complements[target - num] = i

