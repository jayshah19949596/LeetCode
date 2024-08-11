"""
1. Two Sum [EASY]
https://leetcode.com/problems/two-sum
### 1. Question:
----------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### 2. Solution:
----------------------------
Iterate through the previous sequence.  When we see a
different number, append [1, num] to the new sequence.
When we see the same number increment its count.

#### Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#### Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

### 3. Complexity Analysis:
----------------------------
"""

"""
=========================
APPROACH 1: Brute force approach.
Loop through each element x and find if there is another value that equals to target−x.

Time - O(n^2), For each element, we try to find its complement by looping through the rest of the array which takes
Space - O(1)
=========================
"""
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

"""
=========================
APPROACH 2: Sorting with Binary search.
Sort the input array. Loop through each element 'x'. 
For every element 'x', find if there is 'target'−'x' in 'nums' using binary search. 

Time - O(n*Logn), The array is sorted to facilitate the two-pointer technique.
Space - O(n)
=========================
"""
class Solution:
    def bin_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) //2
            mid_num, mid_num_idx = nums[mid]
            if mid_num == target:
                return mid_num_idx
            elif target < mid_num:
                right = mid -1   # Search in left Direction
            else:
                left = mid + 1   # Search in right Direction
        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store number values and their indices because in output we want to return indices of the numbers
        nums_with_indices = [(num, index) for index, num in enumerate(nums)]
        nums_with_indices.sort() # Sort by the number

        for i in range(len(nums_with_indices)):
            num, og_idx = nums_with_indices[i]
            comp_pair = target - num
            comp_idx = self.bin_search(nums_with_indices, comp_pair)

            if comp_idx != -1 and comp_idx != og_idx:
                return [og_idx, comp_idx]


"""
=========================
APPROACH 3: Sorting with Two pointer.
Sort the input array. Loop through each element 'x'. 
Start by choosing the element in two ends in sorted 'nums'. 
Try to find two pairs by either making small element bigger or big element smaller.

Time - O(n+n*Logn), The array is sorted to facilitate the two-pointer technique.
Space - O(n)
=========================
"""
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store number values and their indices because in output we want to return indices of the numbers
        nums_with_indices = [(num, index) for index, num in enumerate(nums)]
        nums_with_indices.sort()  # Sort by the number

        left, right = 0, len(nums_with_indices) - 1

        while left < right:
            left_num, left_index = nums_with_indices[left]
            right_num, right_index = nums_with_indices[right]
            current_sum = left_num + right_num

            if current_sum == target:
                return [left_index, right_index]
            elif current_sum < target:  # the small element is in right direction
                left += 1
            else:  # the big element is in left direction
                right -= 1




"""
=========================
APPROACH 4: Two pass with Dictionary.
To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array.
If the complement exists, we need to get its index.
What is the best way to maintain a mapping of each element in the array to its index? A hash table.
We can reduce the lookup time from O(n) to O(1) by trading space for speed.
A hash table is well suited for this purpose because it supports fast lookup in near constant time.

Time - O(n), We traverse the list containing n elements exactly twice.
Space - O(n), The extra space required depends on the number of items stored in the hash
=========================
"""
class Solution(object):

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_2_index = {}
        for i in range(len(nums)):
            nums_2_index[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_2_index and nums_2_index[complement] != i:
                return [i, nums_2_index[complement]]


"""
=========================
APPROACH 5: One Pass with Dictionary.
To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array.
If the complement exists, we need to get its index.
What is the best way to maintain a mapping of each element in the array to its index? A hash table.
We can reduce the lookup time from O(n) to O(1) by trading space for speed.
A hash table is well suited for this purpose because it supports fast lookup in near constant time.

Time - O(n), We traverse the list containing n elements only once.
Space - O(n), The extra space required depends on the number of items stored in the hash
=========================
"""
class Solution(object):

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_2_index = {}
        for i, num in enumerate(nums):
            if target-num in nums_2_index:
                return [nums_2_index[target-num], i]
            nums_2_index[num] = i
