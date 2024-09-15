"""
629. K Inverse Pairs Array [HARD]
https://leetcode.com/problems/k-inverse-pairs-array

### 1. Question Explanation:
----------------------------
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs.
Since the answer can be huge, return it modulo 109 + 7.

#### Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

#### Example 2:
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

### 2. Solution:
----------------------------
Ref: https://algo.monster/liteproblems/629 ?

### 3. Complexity Analysis:
----------------------------
Time Complexity: ??
Space Complexity: ??
"""
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
