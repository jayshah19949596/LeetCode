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
"""
from bisect import bisect_left
from typing import List


class SummaryRanges:

    def __init__(self):
        self.nums = []

    def addNum(self, value: int) -> None:
        """
        Time Complexity: O(N), bisect will take O(LogN) and list.insert will take O(N)
        Space Complexity: O(N), storing numbers in self.nums takes O(N) space.
        """
        idx = bisect_left(self.nums, value)
        # Below is to handle duplicates. Adding duplicates breaks the code correctness.
        if idx < len(self.nums) and self.nums[idx] == value:
            return
        self.nums.insert(idx, value)

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
