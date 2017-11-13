# Source: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Author: Paulo Lemus
# Date  : 2017-11-12
# Info  : #21, Easy

# Merge two sorted linked lists and return it as a new list. The new
# list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
	"""
	:type l1: ListNode
	:type l2: ListNode
	:rtype: ListNode
	"""
	sorted_list = ListNode(0)
	tail = sorted_list

	# Build the sorted list
	while l1 and l2:
	    if l1.val < l2.val:
		tail.next = l1
		l1 = l1.next
	    else:
		tail.next = l2
		l2 = l2.next
	    tail = tail.next

	while l1:
	    tail.next = l1
	    tail = l1
	    l1 = l1.next

	while l2:
	    tail.next = l2
	    tail = l2
	    l2 = l2.next

	return sorted_list.next

