import random

class Solution:
    # QuickSelect - time: O(n), space: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right, k = 0, len(nums) - 1, len(nums) - k
        while left < right:
            pivot_idx = self.hoare_partition(nums, left, right)
            if pivot_idx == k:
                return nums[k]
            elif pivot_idx < k:
                left = pivot_idx+1
            else:  # pivot_idx > k
                right = pivot_idx-1
        return nums[left]

    def hoare_partition(self, nums, low, high):
        pivot_idx = random.randint(low, high)  # random pivot
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
        i, j = low, high-1
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[i], nums[high] = nums[high], nums[i]  # insert pivot in correct position
        return i
