# Source: https://leetcode.com/problems/max-consecutive-ones/description/
# Author: Paulo Lemus
# Date  : 2017-11-11
# Info  : #485, Easy

# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	maximum = 0
	total = 0

	for num in nums:
	    if num:
		total += 1
	    else:
		maximum = max(maximum, total)
		total = 0

	return max(maximum, total)

