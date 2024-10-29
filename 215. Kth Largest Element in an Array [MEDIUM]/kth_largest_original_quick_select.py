"""
215. Kth Largest Element in an Array [MEDIUM]
This solution is giving - Time Limit Exceeded on LEETCODE
"""
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def lomutos_parititon(arr, low, high):
            i = low
            pivot_idx = high
            pivot_ele = arr[high]

            for j in range(low, high):
                if arr[j]<=pivot_ele:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1    
            
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
            return i
        
        n = len(nums)
        k, left, right =  n-k, 0, n-1
        while left<=right:
            new_pivot_idx = lomutos_parititon(nums, left, right)
            if new_pivot_idx == k:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k:
                right = new_pivot_idx-1
            else:
                left = new_pivot_idx+1
