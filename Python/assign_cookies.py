# Source: https://leetcode.com/problems/assign-cookies/description/
# Author: Paulo Lemus
# Date  : 2017-11-10
# Info  : #455, Easy

# Assume you are an awesome parent and want to give your children
# some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor gi, which is the minimum size of
# a cookie that the child will be content with; and each cookie j has
# a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number
# of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
#
# Example 1:
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1,
# you could only make the child whose greed factor is 1 content.
# You need to output 1.

class Solution:
    def findContentChildren(self, g, s):
	"""
	:type g: List[int]
	:type s: List[int]
	:rtype: int
	"""
	satisfied_children = 0

	g.sort(reverse=True)
	s.sort()

	try:
	    for child in g:
		if child <= s[-1]:
		    # Cookie is big enough
		    satisfied_children += 1
		    s.pop()
	except:
	    pass
	return satisfied_children

