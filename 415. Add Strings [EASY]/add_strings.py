"""
https://leetcode.com/problems/add-strings

### 1. Question Explanation:
----------------------------
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

#### Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

### 2. Complexity Analysis:
----------------------------
Time - O(max(N1,N2))
Space - O(max(N1,N2))
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return self.regular_pythonic_solution(num1, num2)
        return self.mathemetic_solution(num1, num2)

    def regular_pythonic_solution(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

    def mathemetic_solution(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1 = (l2 - l1) * '0' + num1
            l1 = l2
        else:
            num2 = (l1 - l2) * '0' + num2

        carry = 0
        res = ''
        for i in range(l1 - 1, -1, -1):
            s = int(num1[i]) + int(num2[i]) + carry
            carry = s // 10
            res += str(s % 10)

        if carry > 0:
            res += str(carry)
        return res[::-1]
