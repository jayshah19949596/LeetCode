class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
            
        def binary_search(left, right, k):
            while left<=right:
                mid = (left+right)//2
                if nums[mid] == k:
                    return mid
                elif nums[mid]>k:
                    right = mid-1
                else:
                    left = mid+1
            
            return left

        exact = binary_search(0, len(nums)-1, target)
        if target != nums[exact]: return [-1, -1]
        lower = binary_search(0, len(nums)-1, target-0.5)
        upper = binary_search(0, len(nums)-1, target+0.5)
        return [lower, upper-1]
        
