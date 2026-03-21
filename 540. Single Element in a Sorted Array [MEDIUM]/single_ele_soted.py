"""

We use binary search. 
When we find the pair containing mid, we check the size of the remaining left or right section excluding that pair.
If that section has even length, it contains only pairs; if it has odd length, it must contain the single element. 
So we move the search toward the odd-length side.

"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # Case 1: mid forms a pair with the left element
            if mid > 0 and nums[mid] == nums[mid - 1]:
                left_part_len = (mid - 1) - lo
                # If the left part length is EVEN it means it contains only pairs
                # so the single element must be on the right side
                if left_part_len % 2 == 0:
                    lo = mid + 1
                else:
                    hi = mid - 2  # Otherwise the single element must be on the left side

            # Case 2: mid forms a pair with the right element
            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                right_part_len = hi - (mid + 1)

                # If right side length is EVEN it contains only pairs
                # so the single element must be on the left
                if right_part_len % 2 == 0:
                    hi = mid - 1
                else:
                    lo = mid + 2  # Otherwise the single element is on the right

            else:
                # If nums[mid] is not equal to either neighbor,
                # it must be the single element
                return nums[mid]

        # When lo == hi we have found the single element
        return nums[lo]
