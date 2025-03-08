"""
123. Best Time to Buy and Sell Stock III [HARD]
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

Solution: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/editorial/
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_t1_cost, min_t2_cost = float("inf"), float("inf")
        max_t1_profit = max_t2_profit = 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            min_t1_cost = min(min_t1_cost, price)
            max_t1_profit = max(max_t1_profit, price - min_t1_cost)
            # Reinvest the gained profit in the second transaction
            min_t2_cost = min(min_t2_cost, price - max_t1_profit)
            max_t2_profit = max(max_t2_profit, price - min_t2_cost)
        return max_t2_profit
