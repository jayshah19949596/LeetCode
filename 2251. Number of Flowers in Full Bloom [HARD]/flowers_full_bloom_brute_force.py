"""
2251. Number of Flowers in Full Bloom [HARD]

https://leetcode.com/problems/number-of-flowers-in-full-bloom/

### 1. Question Explanation:
----------------------------
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive).
You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

###  Complexity Analysis:
----------------------------
Time Complexity: O(N*M),
    where N = people.length and M = flowers.length
Space Complexity: O(N)
    O(N) stored in "results" array, where N = people.length
"""
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        results = []
        for visiting_day in people:
            bloomed = 0
            start_day = 0
            for bloom_interval in flowers:
                start_bloom_day, end_bloom_day = bloom_interval
                if start_bloom_day<=visiting_day<=end_bloom_day:
                    bloomed += 1
            results.append(bloomed)
        return results
