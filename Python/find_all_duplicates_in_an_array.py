# Source: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #442, Medium, 212 ms, 98.11%

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


class Solution:
    # 328 ms, 41.51%
    def findDuplicates(self, nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	from collections import Counter
	counts = Counter(nums)
	return [i for i in counts if counts[i] == 2]


    # 212 ms, 98.11%
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s = set()
        return [
            num for num in nums if num in s or s.add(num)
        ]

