"""
https://leetcode.com/problems/nested-list-weight-sum/

### 1. Question Explanation:
----------------------------
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
The depth of an integer is the number of lists that it is inside of.
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.


#### Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

#### Example 2:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

#### Example 3:
Input: nestedList = [0]
Output: 0
"""
from collections import deque
from typing import List

class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


# DFS iterative
class Solution:
    def depthSum(self, nested_list: List[NestedInteger]) -> int:
        total = 0

        for i in range(len(nested_list)):
            nested_item = nested_list[i]
            stack = [[1, nested_item]]
            while stack:
                depth, current = stack.pop()
                if current.isInteger():
                    total += current.getInteger() * depth
                else:
                    for item in current.getList():
                        stack.append([depth + 1, item])
        return total


# BFS iterative
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        depth = 1
        total = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nested.getList())
            depth += 1

        return total
