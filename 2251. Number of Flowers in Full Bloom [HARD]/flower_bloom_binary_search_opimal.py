"""
2251. Number of Flowers in Full Bloom
https://leetcode.com/problems/number-of-flowers-in-full-bloom/

### 1. Question Explanation:
----------------------------
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive).
You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.
Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

###  Solution:
----------------------------
Solution Explanation: https://leetcode.com/problems/number-of-flowers-in-full-bloom/editorial/

Algorithm:
1. Create two arrays starts and ends.
2. Iterate over each flower = [start, end] in flowers:
    A} Add start to "starts".
    B} Add end + 1 to "ends".
3. Sort both starts and ends.
4. Initialize the answer array ans and iterate over each person in people:
    A} Perform a binary search on starts for the rightmost insertion index of person to find i.
    B} Perform a binary search on ends for the rightmost insertion index of person to find j.
    C} Add i - j to ans.
5. Return "ans"

###  Complexity Analysis:
----------------------------
Given N as the length of flowers and M as the length of people,
Time complexity: O((N+M)*LogN)
    We first create two arrays of length N, "starts" and "ends", then sort them. This costs O(N*LogN).
    Next, we iterate over "people" and perform two binary searches at each iteration. This costs O(M⋅LogN)
    Thus, our time complexity is O((N+M)*LogN).

Space complexity: O(N)
    "starts" and "ends" both have a size of N.
"""
from typing import List
from bisect import bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends, ans = [], [], []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)

        starts.sort(), ends.sort()

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)

        return ans
