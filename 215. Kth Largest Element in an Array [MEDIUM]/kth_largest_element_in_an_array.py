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
import random
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.sorting_solution(nums, k)
        # return self.heapq_solution(nums, k)
        # return self.heapq_custom_solution(nums, k)
        return self.hoars_selection(nums, k)

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
        APPROACH 3: USING HEAP by pushing in heap and maintaining heap length till K.
        Time complexity: O(N⋅LogN)
        Space complexity: O(K)
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def hoars_selection(self, nums: List[int], k: int) -> int:
        """
        APPROACH 4: Quickselect, also known as Hoare's selection algorithm
        Time complexity: Avg Case: O(N), Worst Case: O(N^2)
        Space complexity: O(N)

        1. Define a quickSelect function that takes arguments nums and k.
        This function will return the kth greatest element in nums
        (the nums and k given to it as input, not the original nums and k).
            - Select a random element as the pivot.
            - Create 'left', 'mid', and 'right' as described above.
            - If 'k <= left.length', return 'quickSelect(left, k)'.
            - If 'left.length + mid.length < k', return 'quickSelect(right, k - left.length - mid.length)'.
            - Otherwise, return pivot.
        2. Call quickSelect with the original 'nums' and 'k', and return the answer.
        """

        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot: left.append(num)
                elif num < pivot: right.append(num)
                else: mid.append(num)

            if len(left) >= k: return quick_select(left + mid, k)
            elif len(left) + len(mid) < k: return quick_select(right, k - len(left) - len(mid))
            elif len(left) + len(mid) == k: return pivot  # mid list has exactly one elements i.e. unique
            elif len(left) + len(mid) > k: return pivot  # mid list has more than one elements i.e. duplicate

        return quick_select(nums, k)
