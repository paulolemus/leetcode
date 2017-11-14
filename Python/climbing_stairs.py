# Source: https://leetcode.com/problems/climbing-stairs/description/
# Author: Paulo Lemus
# Date  : 2017-11-14
# Info  : #70, Easy, 46 ms, 92.35%

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
#
# Example 1:
#
# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.
#
# 1. 1 step + 1 step
# 2. 2 steps

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] *(n)
        return self._topDown(n-1, memo) + self._topDown(n-2, memo)

    def _topDown(self, n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n] != -1:
            return memo[n]

        memo[n] = self._topDown(n-1, memo) + self._topDown(n-2, memo)
        return memo[n]

# 46 ms, 92.35%
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1

        ways = [0] * n
        ways[0], ways[1] = 1, 2

        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n-1]

