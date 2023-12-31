"""
398. Random Pick Index [MEDIUM]
https://leetcode.com/problems/random-pick-index

### 1. Question Explanation:
----------------------------
Given an integer array nums with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

###  Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
import random
from typing import List
from collections import defaultdict



class Solution:

    def __init__(self, nums: List[int]):
        self.num2indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.num2indices[num].append(i)

    def pick(self, target: int) -> int:
        target_indices = self.num2indices[target]
        randomized_idx = random.randint(0, len(target_indices)-1)
        return target_indices[randomized_idx]

