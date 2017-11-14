# Source: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #674, Easy, 62 ms, 95.28%


# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.


# 62 ms, 95.28%
class Solution:
    def findLengthOfLCIS(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	result = 0
	count = 0
	last = float('-inf')

	for num in nums:
	    if num <= last:
		result = max(result, count)
		count = 0
	    last = num
	    count += 1

	return max(result, count)

