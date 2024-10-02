"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii

### 1. Question Explanation:
----------------------------
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

#### Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,|1,1,1,1,1,1|]


### 2. Solution Explanation:
----------------------------
1. Use of a Single Loop
The outer loop iterates through nums using a for loop with right as the index. This simplifies the logic by eliminating the need for a nested loop to adjust left.
2. Count Zeros Efficiently
The code now counts zeros as it expands the window by moving right. If the count of zeros exceeds k, it enters a while loop to increment left until there are at most k zeros in the current window.
3. Update Maximum Length Correctly
The maximum length is updated using right - left + 1, which correctly calculates the size of the current valid window.
4. Removed Unnecessary Print Statements
The print statements were removed to clean up the code, although they can be added back for debugging purposes if needed.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N), where 'N' is total number of element in nums.
Space Complexity: O(1).
"""
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = count_0 = max_len = 0

        for right in range(len(nums)):
            # Count the number of zeros in the current window
            if nums[right] == 0: count_0 += 1

            # If we have more than k zeros, shrink the window from the left
            while count_0 > k:
                if nums[left] == 0: count_0 -= 1
                left += 1

            # Update max_len with the size of the current valid window
            max_len = max(max_len, right - left + 1)

        return max_len