"""
9. Palindrome Number [EASY]
https://leetcode.com/problems/palindrome-number/

1. Question:
----------------------------
Given an integer x, return true if x is a palindrome, and false otherwise.

#### Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

#### Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

2. Complexity Analysis:
----------------------------
Time: O(N), where N is number of digits in argument "x"
Space: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        num, rev = x, 0
        while num > 0:
            rem = num % 10
            rev = 10 * rev + rem
            num = num // 10

        if rev == x: return True
        return False
