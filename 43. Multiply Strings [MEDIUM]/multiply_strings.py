"""
43. Multiply Strings [MEDIUM]
https://leetcode.com/problems/multiply-strings/

### 1. Question:
----------------------------
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#### Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

#### Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088

### 2. Solution:
----------------------------
Reference:
1. https://www.youtube.com/watch?v=O7OA5Kr8CNU&t=899s
2. https://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(m*n), where m and n are length of two number that need to be multiplied.
Auxiliary Space: O(m+n), where m and n are length of two number that need to be multiplied.
"""


class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        if len1 == 0 or len2 == 0 or num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len1 + len2)  # Will keep the result number in vector in reverse order
        i_n1, i_n2 = 0, 0  # These twoindexes are used to find positions in result.

        for i in range(len1 - 1, -1, -1):   # Go from right to left in num1
            carry, n1 = 0, int(num1[i])
            i_n2 = 0  # To shift position to left after every multiplication of a digit in num2
            for j in range(len2 - 1, -1, -1):   # Go from right to left in num2
                n2 = int(num2[j])  # Take current digit of second number
                summ = n1 * n2 + result[i_n1 + i_n2] + carry  # Multiply two digits & add result to previously stored result at current position.
                carry = summ // 10   # Carry for next iteration
                result[i_n1 + i_n2] = summ % 10  # Store result
                i_n2 += 1

            if carry > 0:  # store carry in next cell
                result[i_n1 + i_n2] += carry

            i_n1 += 1  # To shift position to left after every multiplication of a digit in num1.

        # Ignore '0's from the right
        i = len(result) - 1
        while i >= 0 and result[i] == 0:
            i -= 1

        # Generate the result string
        s = ""
        while i >= 0:
            s += str(int(result[i]))
            i -= 1

        return s