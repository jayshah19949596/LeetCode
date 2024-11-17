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
APPROACH-2: Using Heap
------------------------------------------------

### Complexity Analysis:
------------------------------------------------
Time Complexity: O(N*LogK)
Space Complexity: O(K)
"""
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def squared_distance(pt: List[int]) -> int:
            """Calculate and return the squared Euclidean distance."""
            return pt[0] ** 2 + pt[1] ** 2

        heap = []
        for i, point in enumerate(points):
            dist = squared_distance(point)
            heapq.heappush(heap, [-dist, i])
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            element = heapq.heappop(heap)
            dist, idx = element
            result.append(points[idx])
        return result



"""
APPROACH-3: Divide and Conquer with Quick Select:
------------------------------------------------
Sort the "points" array by distance.
Return the first k elements from sorted array.

### Complexity Analysis:
------------------------------------------------
Time Complexity: 
Average case: O(N) because it halves (roughly) the remaining elements needing to be processed at each iteration.
Worst case: O(N^2) in the worst case, where N is the length of points.

Space Complexity: O(N).
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_from_origin(P):
            return P[0] ** 2 + P[1] ** 2

        distances = [[distance_from_origin(points[i]), points[i]] for i in range(len(points))]

        def lomutos_partition(array, low, high):
            partition_idx = high
            partition_ele = array[high]
            i = low
            for j in range(low, high):
                if array[j][0] <= partition_ele[0]:
                    array[i], array[j] = array[j], array[i]
                    i += 1
            array[i], array[partition_idx] = array[partition_idx], array[i]
            return i

        def quick_select(array, low, high, k):
            if low <= high:
                partition_idx = lomutos_partition(array, low, high)
                if partition_idx == k:
                    return array[partition_idx]
                elif partition_idx > k:
                    return quick_select(array, low, partition_idx - 1, k)
                else:
                    return quick_select(array, partition_idx + 1, high, k)

        kth_distance_pt = quick_select(distances, 0, len(distances) - 1, k)
        return [distances[idx][1] for idx in range(0, k)]

"""
APPROACH-4: BinarySearch
------------------------------------------------
1. Precompute the Euclidean distances of each point.
2. Define the initial binary search range by identifying the farthest computed distance.
3. Perform a binary search from low to high using the reference distances.
   - Calculate the midpoint of the remaining range as the target distance.
   - Split the remaining points into those closer and those farther than the target distance.
   - If the closer array has fewer than k points, add them to the closest array and adjust the value of k.
   - Keep only the appropriate remaining array for the next iteration and update the binary search range.
4. Once k elements have been added to the closest array, return the k closest points

### Complexity Analysis:
------------------------------------------------
Time Complexity:
Average case: O(N). It achieves this by halving (on average) the remaining elements needing to be processed at each iteration
Worst case: O(N^2) in the worst case.

Space Complexity: O(N). An extra O(N) space is required for the arrays containing distances and reference indices.
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Precompute the Euclidean distance for each point
        distances = [self.euclidean_distance(point) for point in points]
        # Create a reference list of point indices
        remaining = [i for i in range(len(points))]
        # Define the initial binary search range
        min_dist, max_dist = 0, max(distances)

        # Perform a binary search of the distances
        # to find the k closest points
        closest = []
        while k:
            mid_dist = (min_dist + max_dist) / 2
            closer, farther = self.split_distances(remaining, distances, mid_dist)
            if len(closer) > k:
                # If more than k points are in the closer distances
                # then discard the farther points and continue
                remaining = closer
                max_dist = mid_dist
            else:
                # Add the closer points to the answer array and keep
                # searching the farther distances for the remaining points
                k -= len(closer)
                closest.extend(closer)
                remaining = farther
                min_dist = mid_dist

        # Return the k closest points using the reference indices
        return [points[i] for i in closest]

    def split_distances(self, remaining, distances, mid_dist):
        """Split the distances around the midpoint
        and return them in separate lists."""
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid_dist:
                closer.append(index)
            else:
                farther.append(index)
        return [closer, farther]

    def euclidean_distance(self, point: List[int]) -> float:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
