"""
1868. Product of Two Run-Length Encoded Arrays [MEDIUM]
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays

Solution Reference: https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/solutions/1398600/python-3-two-pointers-clean-one-pass-o-m-n-explanation/
"""
from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = j = freq1 = freq2 = val1 = val2 = 0            # Declare variables
        m, n, ans = len(encoded1), len(encoded2), []
        while i < m or j < n:                              # Starting two pointers while loop
            if not freq1 and i < m:                        # If `freq1 == 0`, assign new value and frequency
                val1, freq1 = encoded1[i]
            if not freq2 and j < n:                        # If `freq2 == 0`, assign new value and frequency
                val2, freq2 = encoded2[j]
            cur_min_freq, product = min(freq1, freq2), val1*val2  # Calculate smaller frequency and product
            if ans and ans[-1][0] == product:              # Update previous frequency if current product is the same.
                ans[-1][1] += cur_min_freq
            else:                                          # Other situation, append new pairs
                ans.append([product, cur_min_freq])
            freq1 -= cur_min_freq                          # Deduct frequency by smaller frequency in current round
            freq2 -= cur_min_freq
            if freq1 == 0: i += 1                          # When frequency is zero, increment pointer by 1
            if freq2 == 0: j += 1
        return ans