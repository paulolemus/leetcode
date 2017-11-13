# Source: https://leetcode.com/problems/implement-queue-using-stacks/description/
# Author: Paulo Lemus
# Date  : 2017-11-13
# Info  : #232, Easy, 62 ms, 48.65%

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in = []
        self._out = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._in.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self._out) == 0:
            for __ in range(len(self._in)):
                self._out.append(self._in.pop())
        return self._out.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self._out) == 0:
            for __ in range(len(self._in)):
                self._out.append(self._in.pop())
        return self._out[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return 0 == len(self._in) == len(self._out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
