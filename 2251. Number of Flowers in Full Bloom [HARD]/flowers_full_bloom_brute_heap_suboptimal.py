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
1. Sort flowers. Create a sorted version of people called sortedPeople.
2. Initialize a hash map dic, a min heap, and an integer i = 0.
3. Iterate over sortedPeople. For each person:
    A}  While flowers[i][0] < person (the flower at i already started blooming),
        push flowers[i][1] (when the flower finishes blooming) to heap and increment i.
    B}  While the top of heap (minimum element) is less than person, pop from heap.
    C}  Set dic[person] to the size of heap.
4. Initialize an array ans. Iterate over people and populate ans using dic.

###  Complexity Analysis:
----------------------------
Given N as the length of flowers and M as the length of people,
Time complexity: O(N*LogN + M*(LogN+LogM))
    We start by sorting both flowers and people. This costs O(N*LogN) and O(M*LogM)respectively.
    Next, we perform O(M) iterations. At each iteration, we perform some heap operations.
    The cost of these operations is dependent on the size of the heap. Our heap cannot exceed a size of N, so these operations cost O(LogN),

    There are some other linear time operations that don't affect our time complexity.
    In total, our time complexity is O(N*LogN + M*(LogN+LogM))

Space complexity: O(N+M)
    We create an array sortedPeople of length M.
    dic also grows to a length of M, and heap can grow to a size of O(N).
"""
import heapq
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers, sorted_people = sorted(flowers), sorted(people)
        dic, heap = {}, []
        i = 0
        for person in sorted_people:

            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1

            while heap and heap[0] < person:
                heapq.heappop(heap)

            dic[person] = len(heap)

        return [dic[person] for person in people]
