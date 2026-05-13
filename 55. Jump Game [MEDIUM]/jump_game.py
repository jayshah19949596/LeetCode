class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1
        
        for i, num in enumerate(nums):
            # 1. SAFETY CHECK: If we are at an index we can't reach, stop.
            if i > max_reach:
                return False
            # 2. UPDATE: See how much further we can jump from here
            max_reach = max(max_reach, i + num)
                            
        return max_reach >= target
