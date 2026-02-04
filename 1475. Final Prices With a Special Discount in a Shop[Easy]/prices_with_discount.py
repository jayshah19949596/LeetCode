class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Create a copy of prices array to store discounted prices
        # result = prices.copy()
        result = []
        stack = []

        for cur_idx, cur_price in enumerate(prices):
            results.append(cur_price)
            # Process items that can be discounted by current price
            while stack and cur_price <= prices[stack[-1]]:
                # Apply discount to previous item using current price
                prv_idx = stack.pop()
                results[prv_idx] = prices[prv_idx] - cur_price
            # Add current index to stack
            stack.append(cur_idx)

        return result
