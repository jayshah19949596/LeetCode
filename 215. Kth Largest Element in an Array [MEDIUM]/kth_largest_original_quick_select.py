"""
215. Kth Largest Element in an Array [MEDIUM]
This solution is giving - Time Limit Exceeded on LEETCODE
"""
from typing import List

class Solution:
    def findKthLargest(self, nums, k):
        def lomutos_partition(array, low, high):
            i = low - 1
            pivot_idx = high
            pivot_element = array[pivot_idx]

            for j in range(low, high):
                if array[j] <= pivot_element:
                    i += 1
                    array[i], array[j] = array[j], array[i]

            array[i + 1], array[pivot_idx] = array[pivot_idx], array[i + 1]
            return i + 1

        left, right = 0, len(nums) - 1
        while True:
            new_pivot_index = partition(nums, left, right)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1
