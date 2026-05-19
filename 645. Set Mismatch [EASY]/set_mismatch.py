"""
Optimized Approach: In Place visit makring 
Time Complexity: O(n) — We pass through the array exactly twice.
Space Complexity: O(1) — We reuse the input array as our state machine store, saving heap memory allocations and maximizing CPU cache locality.
"""
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = [-1] * len(nums)
        dup = miss = -1
        
        for num in nums:
            act_num = abs(num)                
            if nums[act_num - 1] < 0:
                dup = act_num 
            else:
                nums[act_num - 1] = -nums[act_num - 1]  # Mark it as visited
                
        for i, num in enumerate(nums):
            if num>0:
                miss = i+1
                break
        return [dup, miss]
        
from typing import List

"""
Space suboptimized approach: Additional Array to keep track of visited
Time Complexity: O(n) — We pass through the array exactly twice.
Space Complexity: O(n) — We need additional input array visited.
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = [-1] * len(nums)
        dup = miss = -1
        
        for num in nums:
            if seen[num - 1] != -1:
                dup = num  
            visited[num - 1] = 1  
                
        for i, val in enumerate(visited):
            if val == -1:
                miss = i + 1  
                break
                
        return [dup, miss]
