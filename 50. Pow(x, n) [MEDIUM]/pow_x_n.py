"""
50. Pow(x, n) [MEDIUM]
https://leetcode.com/problems/powx-n/

### 1. Question Explanation:
----------------------------
Implement "pow(x, n)", which calculates "x" raised to the power "n" (i.e., x^n).

#### Example 1:
Input: x = 2.10000, n = 3
Output: 9.26100

#### Example 2:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return self.brute_force(x, n)
        # return self.binary_exponential_iterative(x, n)
        return self.binary_exponential_recursive(x, n)

    def brute_force(self, x: float, n: int) -> float:
        """
        Time - O(N)
        Space - O(1)
        """
        pow_ans = 1
        for i in range(n):
            pow_ans = pow_ans * x
        return pow_ans

    def binary_exponential_recursive(self, x: float, n: int) -> float:
        """
        Time - O(LogN)
        Space - O(1)
        """
        if n == 0: return 1
        if n < 0: x, n = 1.0 / x, -n

        if n % 2 == 0:
            temp = self.binary_exponential_recursive(x, n // 2)
            return temp * temp
        else:
            temp = self.binary_exponential_recursive(x, (n - 1) // 2)
            return x * temp * temp

    def binary_exponential_iterative(self, x: float, n: int) -> float:
        """
        Time - O(LogN)
        Space - O(1)
        """
        if n == 0: return 1

        # Handle case where, n < 0.
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2
        return result
