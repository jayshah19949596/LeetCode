from typing import List

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
