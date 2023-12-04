"""
https://leetcode.com/problems/k-closest-points-to-origin/description/

### 1. Question Explanation:
----------------------------
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### 2. Solution Explanation:
----------------------------
Sort the "points" array by distance.
Return the first k elements from sorted array.


### 3. Complexity Analysis:
----------------------------
Time - O(N.LogN)
Space - O(N)
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]
