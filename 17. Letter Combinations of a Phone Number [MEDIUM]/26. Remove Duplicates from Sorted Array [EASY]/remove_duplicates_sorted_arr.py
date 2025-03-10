class Solution:
    def removeDuplicates(self, nums):  # Added 'self' as the first parameter
        anchor_idx=1
        for moving_idx in range(1, len(nums)):
            if nums[moving_idx]!=nums[moving_idx-1]:
                nums[anchor_idx]=nums[moving_idx]
                anchor_idx=anchor_idx+1
        return anchor_idx
