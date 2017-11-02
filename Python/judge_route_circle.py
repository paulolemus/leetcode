# Source: https://leetcode.com/problems/judge-route-circle/description/
# Author: Paulo Lemus
# Date  : 2017-11-01


# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Count each move
        ups = downs = lefts = rights = 0

        for move in moves:
            if move == 'U':
                ups += 1
            elif move == 'D':
                downs += 1
            elif move == 'L':
                lefts += 1
            else:
                rights += 1

        return ups == downs and lefts == rights

