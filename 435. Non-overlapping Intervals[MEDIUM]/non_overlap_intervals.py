from typing import List

"""
Greedy idea
Keep as many intervals as possible by always picking the one that finishes earliest.

Steps:
1. Sort intervals by end time
2. Walk through them, keep an interval if it starts >= last_end
3. Otherwise it overlaps → remove it

This greedy is optimal because choosing the earliest end leaves the most room for future intervals.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # sort by end
        removals = 0
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end          # keep it
            else:
                removals += 1           # remove this interval (the one with later end)

        return removals
