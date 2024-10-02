"""
539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference

============================

## APPROACH 1: Using Sorting
### 1. Solution Explanation:
----------------------------
Intuition
Since the times are given in "HH:MM" string format instead of the number of minutes,
Parse the string format of each time and convert it into the total number of minutes passed since "00:00".
The converted array can be sorted in ascending order, then the minimum difference must be the difference in an adjacent pair of times.
This is because adjacent elements in a sorted array have smaller differences than non-adjacent elements.
Thus, we can sort our array and calculate the difference between each adjacent pair of elements, keeping track of the smallest difference.

### 2. Complexity Analysis:
============================
Time Complexity: O(NlogN)
Space Complexity: O(N)
============================
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert input to minutes
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        # sort times in ascending order
        minutes.sort()

        # find minimum difference across adjacent elements
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))

        # consider difference between last and first element
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])