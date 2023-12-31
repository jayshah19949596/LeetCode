"""
724. Find Pivot Index [Easy]
https://leetcode.com/problems/find-pivot-index

### 1. Question:
---------------------------
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array

### 2. Solution:
---------------------------
We need to quickly compute the sum of values to the left and the right of every index.
Let's say we knew S as the sum of the numbers, and we are at index i. If we knew the sum of numbers left_sum that are to the left of index i, then the other sum to the right of the index would just be S - nums[i] - left_sum.
As such, we only need to know about left_sum to check whether an index is a pivot index in constant time. Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.

### 3. Complexity:
---------------------------
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            right_sum = total_sum - left_sum - x
            if left_sum == right_sum:
                return i
            left_sum += x
        return -1
