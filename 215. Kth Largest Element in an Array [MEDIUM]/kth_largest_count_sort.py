"""
Refer editorial presentation for last approach counting sort : https://leetcode.com/problems/kth-largest-element-in-an-array/editorial/
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_num, min_num = -float("inf"), float("inf") 
        count = defaultdict(int)
        for num in nums:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            count[num] += 1
        remaining = k
        for num in range(max_num, min_num-1, -1):
            remaining -= count[num]
            if remaining<=0: return num
        return nums[0]
