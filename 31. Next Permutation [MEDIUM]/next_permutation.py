"""
31. Next Permutation [MEDIUM]
https://leetcode.com/problems/next-permutation
Ref explaination: https://leetcode.com/problems/next-permutation/solutions/1910236/python-easy-o-n-solution-explained/?envType=company&envId=facebook&favoriteSlug=facebook-six-months

### 1. Question:
----------------------------
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order
Then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

### 2. Solution:
----------------------------
[1, 5, 8, 4, 7, 6, 5, 3, 1]
[1, 5, 8, {4}, 7, 6, 5, 3, 1].    # Find first element in decreasing order from right to left
[1, 5, 8, 4, 7, 6, {5}, 3, 1].    # Find element just larger than {4}
[1, 5, 8, {5}, 7, 6, {4}, 3, 1]   # Swap the two elements found
[1, 5, 8, 5, 1, 3, 4, 6, 7]       # Reverse elements from the swapped element

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(1)
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:  # Find first element in decreasing order from right to left
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:  # Find element just larger than then element in decreasing
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap the two elements found

        nums[i + 1:] = nums[i + 1:][::-1]  # Reverse elements from the swapped element
