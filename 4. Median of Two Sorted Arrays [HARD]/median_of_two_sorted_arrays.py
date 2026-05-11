"""
https://leetcode.com/problems/median-of-two-sorted-arrays
"""
class Solution:
    """
    APPROACH: Binary Search
    ----------------------------
    1. Ensure the first array (nums1) is the smaller one.
    2. Perform binary search on the smaller array to find the correct partition.
    3. Calculate the corresponding partition in the larger array.
    4. Compare elements around the partition to determine if it's correct.
    5. Adjust the partition if necessary and repeat until the correct partition is found.

    COMPLEXITY ANALYSIS:
    ----------------------------
    Time: O(Log(min(m,n))), where m and n are the lengths of the input arrays
    Space: O(1)
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2): nums1, nums2 = nums2, nums1
        x, y, = len(nums1), len(nums2)
        full_len = x+y
        low, high = 0, len(nums1)
        half_len = (full_len+1)//2
        while low<=high:
            pivot_x = (low+high)//2 # nums1[pivot_x] is the first element of the right half
            pivot_y = half_len-pivot_x  # nums2[pivot_y] is the first element of the right half 

            if pivot_x-1 < 0: max_left_x = -float("inf")
            else: max_left_x = nums1[pivot_x-1]

            if pivot_x == x: min_right_x = float("inf")
            else: min_right_x = nums1[pivot_x]

            if pivot_y-1 < 0: max_left_y = -float("inf")
            else: max_left_y = nums2[pivot_y-1]

            if pivot_y == y:  min_right_y = float("inf")
            else: min_right_y = nums2[pivot_y]

            results = max(max_left_x, max_left_y)
            if max_left_x<=min_right_y and max_left_y<=min_right_x:
                if full_len%2 == 1:
                    return results
                else:
                    return (results + min(min_right_x, min_right_y))/2
            elif max_left_x>min_right_y:
                high = pivot_x-1
            else:
                low = pivot_x+1
