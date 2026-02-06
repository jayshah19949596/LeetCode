"""
https://leetcode.com/problems/sliding-window-maximum/

### 1. Question Explanation:
----------------------------
Given an array nums, there is a sliding window of size
k which is moving from the very left of the array to the
very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return a list of the max number in each window of the sliding window.

### 2. Solution Explanation:
----------------------------
Keep indices in double ended queue.  New indices are added
at head of queue (RHS) so oldest are at tail (LHS).
Before adding a new index, pop from tail all indexes
whose numbers are less than the new num since they can
never be the window max.  Pop from head if that index
is now outside the window.  Head has largest in window.

### 3. Complexity Analysis:
----------------------------
Time - O(n)
Space - O(k)
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()  # deque acts as a monotonic decreasing queue
        results = []

        for i, num in enumerate(nums):

            while queue and nums[queue[-1]] < num:  # pop smaller numbers from RHS
                queue.pop()

            queue.append(i)  # append this number at RHS

            if i-queue[0] >= k:  # if LHS is outside window, remove it
                queue.popleft()

            if i >= k - 1:  # if window is at least k, add LHS to result
                results.append(nums[queue[0]])

        return results



