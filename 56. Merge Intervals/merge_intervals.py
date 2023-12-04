"""
https://leetcode.com/problems/merge-intervals/

### 1. Question Explanation:
----------------------------
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

#### Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

#### Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

### 2. Complexity Analysis:
----------------------------
Time Complexity - O(N.LogN)
Space Complexity - O(N)
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_start, prev_end = merged_intervals[-1]

            if prev_end >= cur_start:
                merged_intervals[-1][1] = max(prev_end, cur_end)
            else:
                merged_intervals.append(intervals[i])

        return merged_intervals