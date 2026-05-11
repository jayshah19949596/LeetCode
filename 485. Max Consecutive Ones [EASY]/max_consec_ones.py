class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_ones = max_ones = 0
        for num in nums:
            if num == 1: cur_ones += 1
            else: cur_ones = 0
            max_ones = max(max_ones, cur_ones)
        return max_ones
