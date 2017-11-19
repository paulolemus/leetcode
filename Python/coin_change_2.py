# Source: https://leetcode.com/problems/coin-change-2/description/
# Author: Paulo Lemus
# Date  : 2017-11-18
# Info  : #518, Medium

# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
# Note: You can assume that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1


class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        combinations = [0] * (amount+1)
        combinations[0] = 1

        for coin in coins:
            for i in range(1, amount+1):
                sub = i - coin
                combinations[i] += 0 if sub < 0 else combinations[sub]

        return combinations[amount]

