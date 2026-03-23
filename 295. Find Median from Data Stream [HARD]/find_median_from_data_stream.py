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

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        # Max-heap (stores smaller half, use negative numbers)
        self.small_max_heap = [] 
        # Min-heap (stores larger half)
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        # Overall logic: Left -> Right -> Rebalance
        # Step 1: Always push to max-heap (left), then move the largest in left to min-heap (right)
        # This automatically "sorts" the new number into the correct half
        heappush(self.small_max_heap, -num)
        heappush(self.large_min_heap, -heappop(self.small_max_heap))
        
        # Step 2: Rebalance if the right side gets larger than the left
        # We want small_max_heap to always be >= large_min_heap in size
        if len(self.large_min_heap) > len(self.small_max_heap):
            heappush(self.small_max_heap, -heappop(self.large_min_heap))

    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return float(-self.small_max_heap[0])
        return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2.0


class MedianFinder:

    def __init__(self):
        self.higher = [] # contains values in right side of median
        self.lower = [] # contains values in left side of median

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
