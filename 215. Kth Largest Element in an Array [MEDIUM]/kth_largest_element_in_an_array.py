"""
https://leetcode.com/problems/basic-calculator-ii/

### 1. Question Explanation:
----------------------------
Given an integer array "nums" and an integer "k", return the "kth" largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

#### Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

#### Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.sorting_solution(nums, k)
        # return self.heapq_solution(nums, k)
        return self.heapq_custom_solution(nums, k)

    def sorting_solution(self, nums, k):
        """
        APPROACH 1: SORTING
        Time complexity: O(N⋅LogN)
        Space complexity: O(N)
        """
        nums = sorted(nums)
        return nums[-k]

    def heapq_solution(self, nums, k):
        """
        APPROACH 2: USING HEAP with nlargest function
        Time complexity: O(N⋅LogN)
        Space complexity: O(K)
        """
        return heapq.nlargest(k, nums)[-1]

    def heapq_custom_solution(self, nums, k):
        """
        APPROACH 2: USING HEAP by pushing in heap and maintaining heap length till K.
        Time complexity: O(N⋅LogN)
        Space complexity: O(K)
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
