"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

### 1. Question Explanation:
----------------------------
There are "n" buildings in a line. You are given an integer array "heights" of size "n" that represents the heights of the buildings in the line.
The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions.
Formally, a building has an ocean view if all the buildings to its right have a smaller height.
Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

#### Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

#### Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

#### Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

### 2. Solution Explanation:
----------------------------
Start linear iteration from right side.
Track the height of tallest building seen so far.
Compare the height of current building with tallest building.
If current building height is tall then it can see the ocean view. Update the tallest building seen so far with current building height.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(1)
"""

from collections import deque
from typing import List

# =================================
# Approach - 1: Traversing Reverse
# =================================
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height_until_now = heights[-1]
        results = deque([len(heights)-1])
        for i in range(len(heights)-2, -1, -1):
            current_hight = heights[i]
            if current_hight > max_height_until_now:
                results.appendleft(i)
                max_height_until_now = current_hight
        return results


# =============================
# Approach - 2: Using stack
# =============================
from collections import deque
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        results = []
        for i in range(len(heights)):
            while results and heights[i]>=heights[results[-1]]:
                results.pop()
            results.append(i)
        return results
