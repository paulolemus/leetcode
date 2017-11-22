# Source: https://leetcode.com/problems/same-tree/description/
# Author: Paulo Lemus
# Date  : 2017-11-19
# Info  : #100, Easy, 49 ms, 87.07%

# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 49 ms, 87.07%
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ltree = [p]
        rtree = [q]

        while ltree and rtree:
            lside = ltree.pop()
            rside = rtree.pop()

            # Both nodes exist, compare and push children
            if lside and rside:
                if not lside.val == rside.val:
                    return False
                ltree.append(lside.left)
                ltree.append(lside.right)
                rtree.append(rside.left)
                rtree.append(rside.right)
            elif lside or rside:
                return False

        return len(ltree) == 0 and len(rtree) == 0

