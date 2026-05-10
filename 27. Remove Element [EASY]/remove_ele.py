class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        anchor_idx = 0
        for moving_idx in range(len(nums)):
            if nums[moving_idx] != val:
                nums[anchor_idx] = nums[moving_idx]
                anchor_idx += 1
        return anchor_idx
