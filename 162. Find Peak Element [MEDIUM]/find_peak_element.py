"""
https://leetcode.com/problems/find-peak-element/

### 1. Question Explanation:
----------------------------
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1],
find a peak element and return its index.
The array may contain multiple peaks, in that case
return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return self.linear_search_brute_force(nums)
        return self.binary_search_peak_iterative(nums)
        # return self.binary_search_peak_recursive(nums)

    def linear_search_brute_force(self, nums: List[int]) -> int:
        """
        Linear search the array. Compare teh current element with it's neighbor to identify the peak

        Time - O(N)
        Space - O(1)
        """
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0

        for i in range(1, len(nums) - 1):
            prev_num, cur_num, nxt_num = nums[i - 1], nums[i], nums[i + 1]
            if cur_num > prev_num and cur_num > nxt_num:
                return i

        if nums[-1] > nums[-2]: return len(nums) - 1

    def binary_search_peak_iterative(self, nums: List[int]) -> int:
        """
        If array has 3 or more elements, return middle if it is a peak
        Else search for peak on the side which has bigger neighbor of middle indexed element.
        If array has < 3 elements, return index of greater.

        Time - O(LogN)
        Space - O(1)
        """
        left, right = 0, len(nums)-1
        
        while left<right:
            mid = (left + right)//2
            if ((mid==0 and nums[mid]>nums[mid+1]) or
               (mid == len(nums)-1 and nums[mid]>nums[mid-1]) or
               (nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1])):
                return mid
            elif nums[mid+1]>nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return left

    def binary_search_peak_recursive(self, nums, left, right):
        """
        If array has 3 or more elements, return middle if it is a peak
        Else search for peak on the side which has bigger neighbor of middle indexed element.
        If array has < 3 elements, return index of greater.

        Time - O(LogN)
        Space - O(1)
        """
        if left > right:
            return

        mid = (left + right) // 2

        if (
                ((mid > 0) and (mid < len(nums) - 1) and (nums[mid] > nums[mid + 1]) and (nums[mid] > nums[mid - 1]))
                or ((mid == 0) and (nums[mid] > nums[mid + 1]))
                or ((mid == len(nums) - 1) and (nums[mid] > nums[mid - 1]))
        ):
            return mid

        elif nums[mid] < nums[mid + 1]:
            return self.binary_search(nums, mid + 1, right)

        return self.binary_search(nums, left, mid - 1)

