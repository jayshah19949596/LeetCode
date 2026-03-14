"""
We solve this problem using a modified binary search because the array is originally sorted but then rotated. 
At any step of binary search, at least one half of the array must still be sorted.
We compute the middle index and first check if the middle element is the target. 
If not, we determine which half is sorted by comparing nums[left] with nums[mid]. 
If nums[left] <= nums[mid], the left half is sorted. We then check whether the target lies within this sorted range. 
If it does, we continue searching in the left half; otherwise, we search in the right half. 
If the left half is not sorted, then the right half must be sorted, and we similarly check whether the target lies within the sorted right range to decide which side to discard.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
