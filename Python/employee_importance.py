# Source: https://leetcode.com/problems/employee-importance/discuss/
# Author: Paulo Lemus
# Date  : 2017-11-18
# Info  : #690, 325 ms, 78.49%

# You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.
#
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
#
# Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.


"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importanceself.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees = {employee.id: employee for employee in employees}
        stack = []
        total_importance = 0

        stack.append(employees[id])

        while len(stack):
            employee = stack.pop()
            total_importance += employee.importance
            for subordinate in employee.subordinates:
                stack.append(employees[subordinate])

        return total_importance

