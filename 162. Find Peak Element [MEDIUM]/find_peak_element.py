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

### 2. Solution Explanation:
----------------------------
If array has 3 or more elements, return middle if it is a peak
Else search for peak on the side which has bigger neighbor of middle indexed element.
If array has < 3 elements, return index of greater.

### 3. Complexity Analysis:
----------------------------
Time - O(LogN)
Space - O(1)
"""
from typing import List


class Solution(object):
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right - 1:  # at least 3 elements

            mid = (left + right) // 2

            if nums[mid] >= nums[mid + 1] and nums[mid] >= nums[mid - 1]:
                return mid
            if nums[mid + 1] > nums[mid]:  # RHS is higher (LHS could be also but arbitrarily choose RHS)
                left = mid + 1
            else:  # LHS must be higher if RHS is not
                right = mid - 1

        if nums[left] >= nums[right]:
            return left
        return right


class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.binary_search(nums, 0, len(nums) - 1)

    def binary_search(self, nums, left, right):
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

