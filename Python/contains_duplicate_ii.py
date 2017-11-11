# Source: https://leetcode.com/problems/contains-duplicate-ii/description/
# Author: Paulo Lemus
# Date  : 2017-11-11
# Info  : #219, Easy

# Given an array of integers and an integer k, find out whether there are
# two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	duplicates = {}

	for i, num in enumerate(nums):
	    if num in duplicates:
		if abs(duplicates[num] - i) <= k:
		    return True
		else:
		    duplicates[num] = i
	    else:
		duplicates[num] = i
	return False

