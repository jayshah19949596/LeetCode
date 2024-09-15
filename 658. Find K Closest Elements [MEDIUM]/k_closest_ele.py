"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements

### 1. Question Explanation:
----------------------------
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""

"""
============================
# APPROACH 1: Quickselect with Lomutos Partition
============================

### 1. Solution Explanation:
----------------------------

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N), in avg case. O(N^2) in worst case. Worst case probability is negligible.
Space Complexity: O(N)
"""
from collections import deque
class Solution:
    def findClosestElements(self, array: List[int], k: int, x: int) -> List[int]:

        def partition(arr, low, high):
            i = low - 1
            part_idx = high
            part_ele = arr[part_idx][1]
            for j in range(low, high):
                if arr[j][1] <= part_ele:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[part_idx] = arr[part_idx], arr[i+1]
            return i + 1

        def create_dist_arr(arr, k, x):
            dist_array = [[ele, abs(ele-x)] for i, ele in enumerate(arr)]
            return dist_array

        dist_arr = create_dist_arr(array, k, x)
        left, right = 0, len(dist_arr)-1
        while left <= right:
            new_part_idx = partition(dist_arr, left, right)
            if new_part_idx == k: break
            elif new_part_idx > k: right = new_part_idx - 1
            else: left = new_part_idx + 1

        # result_arr = deque([])
        # for i in range(k):
        #     ele = dist_arr[i][0]
        #     if len(result_arr) == 0 or result_arr[-1] > ele: result_arr.appendleft(ele)
        #     else: result_arr.append(ele)

        result_arr = [dist_arr[i][0] for i in range(k)]
        return sorted(result_arr)

"""
============================
# APPROACH 2: Binary Search + Sliding Window Expansion
============================

### 1. Solution Explanation:
----------------------------
As a base case, if arr.length == k, return arr.
Use binary search to find the index of the closest element to x in arr. Initailize two pointers left and right, with left set equal to this index, and right equal to this index plus one.
While the window's size is less than k, check which number is closer to x: arr[left] or arr[right]. Whichever pointer has the closer number, move that pointer towards the edge to include that element in our output.
Return the elements inside arr contained within the window defined between left and right

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(log(N)+k)
Space Complexity: O(N)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k: return arr

        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1
        # While the window size is less than k
        while right - left - 1 < k:
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or (abs(arr[left] - x) <= abs(arr[right] - x) and left != -1):
                left -= 1
            elif left == -1 or abs(arr[left] - x) > abs(arr[right] - x):
                right += 1

        # Return the window
        return arr[left + 1:right]
