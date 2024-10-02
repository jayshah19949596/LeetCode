"""
670. Maximum Swap [MEDIUM]
https://leetcode.com/problems/maximum-swap/

Solution REF: https://leetcode.com/problems/maximum-swap/solutions/4266278/easy-to-understand-python3-code-with-full-explanation-o-n-time-o-n-space/

### 1. Question Explanation:
----------------------------
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

#### Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

#### Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

### 2. Solution Explanation:
----------------------------
APPROACH: Greedy Approach
Intuition is to swap the smallest left-most digit with the largest right-most digit in order to maximize the number
We iterate from right to left, we have to keep track of the largest digit encountered so far and then swap it with left-most digit which is smaller than it.

This is greedy approach Because we are guaranteed to find the right-most largest digit and replace it with the left-most smallest digit.
Since this is a greedy approach, we don't need any look backs and only need to iterate through all the digits just once.


### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))

        # initialize tuple which stores value of maximum digit and its index and set this to rightmost digit
        max_digit = (int(num_list[len(num_list) - 1]), len(num_list) - 1)

        # initialize tuple which stores indices of digits to be swapped
        swap_indices = (0, 0)

        # iterate through the number list from right to left
        for idx in range(len(num_list) - 2, -1, -1):
            digit = int(num_list[idx])

            # if current digit is smaller than max digit, register current index to be swapped with index of max digit encounted so far
            if digit < max_digit[0]:
                swap_indices = (max_digit[1], idx)
            # if current digit is greater than max digit, register new max_digit
            elif digit > max_digit[0]:
                max_digit = (digit, idx)

            # if the current digit is equal to max digit, then don't make any changes because we always want to swap rightmost largest digit

        # swap digits
        num_list[swap_indices[0]], num_list[swap_indices[1]] = num_list[swap_indices[1]], num_list[swap_indices[0]]
        return(int(''.join(num_list)))
