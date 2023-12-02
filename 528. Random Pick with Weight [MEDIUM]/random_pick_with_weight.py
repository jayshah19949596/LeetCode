"""
https://leetcode.com/problems/random-pick-with-weight/

### 1. Question Explanation:
----------------------------
Given an array w of positive integers, where w[i] describes
the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.

### 2. Solution Explanation:
----------------------------
Create a list of cumulative weights. Choose a random integer
between 1 and the sum of all weights. Binary search the
cumulative list for the index where the random integer
would be inserted and return that index. Probability of
choosing an index is proportional to its weight.

Explanation of why prefixSum works:
Think that if we had an array [1,2,3,4,3]. Normal random pickIndex would pick any index from 0 to 4 with equal probability.
But we want that index=1 is picked by 2/13 probability, index=0 with 1/13 probability and so on. (13 is sum of weights).
To ensure that one way to think of it if we make a larger array (of size 13) where the values are the indices such that index i is repeated w[i] times.
Then if we do a normal rand on this array then index 0 to 12 will be picked randomly with equal probability.
13 index array -> [0, 1,1, 2,2,2, 3,3,3,3, 4,4,4]. So there is a 3/13 chance of picking 2 as 2 is repeated thrice in the new array.


### 3. Complexity Analysis:
----------------------------
Time Complexity:
- O(N) of constructor function for number of weights N.
- O(N) for pickIndex function.
- O(logN) for pickIndexBinary function.

Space Complexity: O(N)
"""
import random
from typing import List


class Solution(object):

    def __init__(self, w: List[int]):
        self.cumulative = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.cumulative.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # target = random.randint(1, self.cumulative[-1])
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.cumulative):
            if target <= prefix_sum:
                return i

    def pickIndexBinary(self) -> int:
        target = self.total_sum * random.random()
        # target = random.randint(1, self.cumulative[-1])
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


"""
Your Solution object will be instantiated and called as such:
obj = Solution(w)
param_1 = obj.pickIndex()
"""