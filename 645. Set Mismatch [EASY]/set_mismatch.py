from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = [-1] * len(nums)
        dup = miss = -1
        
        for num in nums:
            if seen[num - 1] != -1:
                dup = num  
            seen[num - 1] = 1  
                
        for i, val in enumerate(seen):
            if val == -1:
                miss = i + 1  
                break
                
        return [dup, miss]
