# Source: https://leetcode.com/problems/permutations/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #46, Medium

# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


from itertools import permutations

# 82 ms, 69.17%
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))

