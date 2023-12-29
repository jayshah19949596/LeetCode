"""
121. Best Time to Buy and Sell Stock [EASY]
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

### 1. Question Explanation:
----------------------------
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### 2. Solution Explanation:
----------------------------
The points of interest are the peaks and valleys in the given graph. We need to find the largest price following each valley, which difference could be the max profit.
We can maintain two variables - 'min_price' and 'max_profit' corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N).
Space Complexity: O(1).
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)

        return max_profit
