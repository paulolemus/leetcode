# Source: https://leetcode.com/problems/single-number-iii/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #260, Medium

# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        for num in nums:
            s.remove(num) if num in s else s.add(num) for num in nums
        return list(s)

