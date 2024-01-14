"""
352. Data Stream as Disjoint Intervals [HARD]
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

### 1. Question Explanation:
----------------------------
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:
1. SummaryRanges(): Initializes the object with an empty stream.
2. void addNum(int value): Adds the integer value to the stream.
3. int[][] getIntervals(): Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.

### Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
"""
from typing import List
from sortedcontainers import SortedList


class SummaryRanges:

    def __init__(self):
        self.nums = SortedList()
        self.numsset = set([])

    def addNum(self, value: int) -> None:
        """
        Time Complexity: O(LogN),
                SortedList is similar to TreeSet in Java implemented with AVL tree or red black tree
                So adding in SortedList is O(LogN).
                Ref: https://stackoverflow.com/questions/63430867/time-complexity-of-operations-in-sortedlist-python
        Space Complexity: O(N), storing numbers in self.nums takes O(N) space.
        """
        if value not in self.numsset:
            self.numsset.add(value)
            self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        """
        Time Complexity: O(N), going through all elements in "self.nums" takes O(N).
        Space Complexity: O(N), storing numbers in "intervals" takes O(N) space.
        """
        intervals, i = [], 0
        while i < len(self.nums):
            start = self.nums[i]
            while i + 1 < len(self.nums) and self.nums[i] + 1 == self.nums[i + 1]:
                i += 1
            end = self.nums[i]
            intervals.append([start, end])
            i += 1
        return intervals

