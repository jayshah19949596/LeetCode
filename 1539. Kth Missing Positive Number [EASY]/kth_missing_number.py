"""
1539. Kth Missing Positive Number [EASY]
https://leetcode.com/problems/kth-missing-positive-number

"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers  which are missing before arr[pivot]
            # is less than k --> continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1
        print(right, left, arr[right], arr[left])
        """
        At the end of the loop, left = right + 1. The kth missing is in-between arr[right] and arr[left].
        The number of integers missing before arr[right] is arr[right] - right - 1 -->
        the number to return is arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k
        return arr[right] + k - (arr[right] - right - 1)
        consider example as 1,2,3,4,5
        consider k =3
        arr[right] + k = 5+ 3 = 8 so 8 should be returned but before returning we make sure we remove missing elements before arr[right] i.e. 5
        """
        return k + right + 1