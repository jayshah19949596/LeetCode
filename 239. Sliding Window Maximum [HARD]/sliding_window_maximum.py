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
        queue_window = deque()
        max_window_results = []

        for i, num in enumerate(nums):

            while queue_window and nums[queue_window[-1]] < num:  # pop smaller numbers from RHS
                queue_window.pop()

            queue_window.append(i)  # append this number at RHS

            if i-queue_window[0] >= k:  # if LHS is outside window, remove it
                queue_window.popleft()

            if i >= k - 1:  # if window is at least k, add LHS to result
                max_window_results.append(nums[queue_window[0]])

        return max_window_results

