class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(x):
            left, right = 0, len(nums)
            
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x: left = mid + 1
                else: right = mid
                    
            return left
        
        left = binary_search(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        return [left, binary_search(target + 1) - 1]
