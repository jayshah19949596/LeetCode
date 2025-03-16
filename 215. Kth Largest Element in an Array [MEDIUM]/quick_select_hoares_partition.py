import random
import heapq

class Solution:
    # QuickSelect - time: O(n), space: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        left, right = 0, len(nums)-1
        while left<right:
            pivotIndex = self.hoarePartition(nums, left, right)
            if pivotIndex == k:
                return nums[k]
            elif pivotIndex < k:
                left = pivotIndex+1
            else: # pivotIndex > k
                right = pivotIndex-1
        return nums[left]

    def hoarePartition(self, nums: List[int], left: int, right: int) -> int:
        def swap(i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]
        pivotIndex = random.randint(left, right) # random pivot
        pivot = nums[pivotIndex]
        swap(pivotIndex, right)
        i, j = left, right-1
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            swap(i, j)
            i += 1
            j -= 1
        swap(i, right) # insert pivot in correct position
        return i
