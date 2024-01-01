"""
1868. Product of Two Run-Length Encoded Arrays [MEDIUM]
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

### 1. Question Explanation:
----------------------------
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times

### 2. Solution Explanation:
----------------------------
Simulation

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""
from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def decode(encoding):
            decoding = []
            for enocded_ele in encoding:
                num, num_count = enocded_ele
                for i in range(num_count):
                    decoding.append(num)
            return decoding

        def encode(decoding):
            i, enocoding = 0, []
            while i < len(decoding):
                num, count = decoding[i], 1
                while i < len(decoding) - 1 and decoding[i] == decoding[i + 1]:
                    count, i = count + 1, i + 1
                enocoding.append([num, count])
                i += 1
            return enocoding

        decoded1, decoded2 = decode(encoded1), decode(encoded2)
        new_decoded = [decoded1[i] * decoded2[i] for i in range(len(decoded1))]
        return encode(new_decoded)
