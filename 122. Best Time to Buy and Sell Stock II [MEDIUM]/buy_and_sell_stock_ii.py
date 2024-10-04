"""
122. Best Time to Buy and Sell Stock II [MEDIUM]
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Solution: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/editorial/
Consecutive Peak & Valley
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        peak = valley = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit