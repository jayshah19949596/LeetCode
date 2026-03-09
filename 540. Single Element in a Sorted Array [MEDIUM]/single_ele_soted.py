class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if mid > 0 and nums[mid] == nums[mid - 1]:
                left_part_len = (mid-1) - lo   # includes the pair ending at mid
                if left_part_len % 2 == 0:
                    lo = mid + 1
                else:
                    hi = mid - 2

            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                right_part_len = hi - (mid+1)  # includes the pair starting at mid
                if right_part_len % 2 == 0:
                    hi = mid - 1
                else:
                    lo = mid + 2

            else:
                return nums[mid]

        return nums[lo]
