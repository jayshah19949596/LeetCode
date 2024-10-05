class Solution:
    """
    APPROACH: Binary Search
    ----------------------------
    1. Ensure the first array (nums1) is the smaller one.
    2. Perform binary search on the smaller array to find the correct partition.
    3. Calculate the corresponding partition in the larger array.
    4. Compare elements around the partition to determine if it's correct.
    5. Adjust the partition if necessary and repeat until the correct partition is found.
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2): nums1, nums2 = nums2, nums1
        x, y, = len(nums1), len(nums2)
        low, high = 0, len(nums1)
        half_len = (x+y+1)//2
        while low<=high:
            partition_x = (low+high)//2
            partition_y = half_len-partition_x

            if partition_x == 0: max_left_x = -float("inf")
            else: max_left_x = nums1[partition_x-1]

            if partition_x == x: min_right_x = float("inf")
            else: min_right_x = nums1[partition_x]

            if partition_y == 0: max_left_y = -float("inf")
            else: max_left_y = nums2[partition_y-1]

            if partition_y == y:  min_right_y = float("inf")
            else: min_right_y = nums2[partition_y]

            results = max(max_left_x, max_left_y)
            if max_left_x<=min_right_y and max_left_y<=min_right_x:
                if (x+y)%2 == 1:
                    return results
                else:
                    return (results + min(min_right_x, min_right_y))/2
            elif max_left_x>min_right_y:
                high = partition_x-1
            else:
                low = partition_x+1