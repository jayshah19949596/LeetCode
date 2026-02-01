class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Create a copy of prices array to store discounted prices
        # result = prices.copy()
        result = []
        stack = []

        for i in range(len(prices)):
            result.append(prices[i])
            # Process items that can be discounted by current price
            while stack and prices[stack[-1]] >= prices[i]:
                # Apply discount to previous item using current price
                result[stack.pop()] -= prices[i]
            # Add current index to stack
            stack.append(i)

        return result
