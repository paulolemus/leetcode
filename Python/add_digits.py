# Source: https://leetcode.com/problems/add-digits/description/
# Author: Paulo Lemus
# Date  : 2017-11-16
# Info  : #258, Easy, 92 ms, 92.50%

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 96 ms, 75%
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = sum(map(int, str(num)))
        return num

# 92 ms, 92.50%
class Solution2:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = num // 10 + num % 10
        return num

