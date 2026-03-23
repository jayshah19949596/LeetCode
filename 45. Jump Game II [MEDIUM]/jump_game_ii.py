class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        # memo[i] will store the min jumps to reach the end from index i
        memo = {}

        def dfs_solve(idx):
            # Base Case: already at or past the last index
            if idx >= n - 1: return 0
            if idx in memo: return memo[idx]

            res = float('inf')
            # Try every possible jump from the current index
            for jump_len in range(1, nums[idx] + 1):
                res = min(res, 1 + dfs_solve(idx + jump_len))

            memo[idx] = res
            return res

        result = dfs_solve(0)
        return result if result != float('inf') else -1


class Solution(object):
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0

        max_index = start = end = 0   # indices in nums of current range
        steps = 1

        while True:         # will always terminate since last index is accessible
            for i in range(start, end+1):
                max_index = max(max_index, i+nums[i])
                if max_index>=len(nums)-1:
                    return steps
            steps += 1
            start, end = end+1, max_index
        return -1
