"""
973. K Closest Points to Origin [MEDIUM]
https://leetcode.com/problems/k-closest-points-to-origin/description/

### 1. Question Explanation:
----------------------------
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""
from typing import List
import math


"""
APPROACH-1: Sorting Solution:
----------------------------
Sort the "points" array by distance.
Return the first k elements from sorted array.

### Complexity Analysis:
----------------------------
Time - O(N.LogN)
Space - O(N)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(P):
            return P[0]**2 + P[1]**2
        points.sort(key=lambda point: distance_from_origin(point))
        return points[:k]

"""
APPROACH-1: Divide and Conquer with Quick Select:
------------------------------------------------
Sort the "points" array by distance.
Return the first k elements from sorted array.

### Complexity Analysis:
------------------------------------------------
Time Complexity: 
O(N) in average case and O(N^2) in the worst case, where N is the length of points.

Space Complexity: O(N)O(N)O(N).
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(P):
            return P[0] ** 2 + P[1] ** 2

        distances = [[distance_from_origin(points[i]), points[i]] for i in range(len(points))]

        def partition(array, low, high):
            partition_idx = high
            partition_ele = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j][0] <= partition_ele[0]:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[partition_idx] = array[partition_idx], array[i + 1]
            return i + 1

        def quick_select(array, low, high, k):
            if low <= high:
                partition_idx = partition(array, low, high)
                if partition_idx == k:
                    return array[partition_idx]
                elif partition_idx > k:
                    return quick_select(array, low, partition_idx - 1, k)
                else:
                    return quick_select(array, partition_idx + 1, high, k)

        kth_distance_pt = quick_select(distances, 0, len(distances) - 1, k)
        return [distances[idx][1] for idx in range(0, k)]


