"""
https://leetcode.com/problems/find-median-from-data-stream

### Question Explanation:
----------------------------
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
The median is the mean of the two middle values.

### Complexity Analysis:
----------------------------
Time complexity: O(LogN)
Space complexity: O(N)
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.higher = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:  # push onto appropriate heap
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)

        if len(self.lower) > 1 + len(self.higher):
            heapq.heappush(self.higher, -heapq.heappop(self.lower))
        elif len(self.higher) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.higher))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        return (-self.lower[0] + self.higher[0]) / 2.0
