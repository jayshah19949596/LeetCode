"""
2817. Minimum Absolute Difference Between Elements With Constraint [MEDIUM]
https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

### 1. Question:
----------------------------
You are given a 0-indexed integer array nums and an integer x.
Find the minimum absolute difference between two elements in the array that are at least x indices apart.
In other words, find two indices i and j such that abs(i - j) >= x and abs(nums[i] - nums[j]) is minimized.
Return an integer denoting the minimum absolute difference between two elements that are at least x indices apart.

 ### 2. Solution:
----------------------------
Reference:
1] https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/solutions/3901967/binary-search-python-beats-100-of-submissions/
2] https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/solutions/3901678/sliding-window-with-sortedlist-o-nlog-n-time-complexity-o-n-space-complexity/

1] We first create a new "sorted_arr" which is an empty list that will eventually store a sorted list.
2] j and i represent the left and right pointer respectively.
>> Intuition: For diff to be minimum between nums[j] and element in sorted_arr, nums[j] has to be close to the element in sorted_arr.
              sorted_arr is constrainted window for nums[j]
3] As we loop through nums, we find the position where nums[j] bisects arr, and insert it.
4] We then find the position where nums[i] bisects arr.
   4a] If it bisects at the end, it is the largest element of the sorted arr and we update ans to be the minimum of the original ans or the difference between nums[i] and the largest element in arr.
   4b] If it bisects at index 0, it is the smallest element of the sorted arr and we update ans accordingly (compared against the smallest element in arr).
   4c] Else it is somewhere in the middle and we will check for the minimum between the elements left and right of it in arr.
"""
from sortedcontainers import SortedList
from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        j, n = 0, len(nums)
        sorted_arr, ans = SortedList(), float('inf')

        for i in range(x, n):
            # https://stackoverflow.com/questions/63430867/time-complexity-of-operations-in-sortedlist-python
            sorted_arr.add(nums[j])
            idx = sorted_arr.bisect_left(nums[i])
            ans = min(ans, abs(nums[i] - sorted_arr[min(len(sorted_arr)-1, idx)]), abs(nums[i] - sorted_arr[max(0, idx-1)]))
            j = j + 1

        return ans
