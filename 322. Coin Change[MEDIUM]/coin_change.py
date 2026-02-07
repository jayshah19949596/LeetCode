from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo[remained] stores the minimum coins needed for remainder amount
        memo = {}

        def dfs(remainder: int) -> int:
            if remainder == 0: return 0
            if remainder < 0: return float("inf")
            if remainder in memo: return memo[remainder]

            best_res = float("inf")
            for coin in coins:
                result = dfs(remainder - coin)
                best_res = min(best, result + 1)

            memo[remainder] = best_res
            return best_res

        ans = dfs(amount)
        return -1 if ans == float("inf") else ans
