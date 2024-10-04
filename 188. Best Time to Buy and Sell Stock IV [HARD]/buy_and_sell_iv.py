"""
188. Best Time to Buy and Sell Stock IV [HARD]
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

Solution: Extension of https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/editorial/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/editorial/

"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0: return 0
        profit = [0 for i in range(k+1)]
        cost = [float("inf") for i in range(k+1)]
        for price in prices:
            for i in range(k):
                cost[i+1] = min(cost[i+1], price-profit[i])
                profit[i+1] = max(profit[i+1], price-cost[i+1])
        return profit[k]