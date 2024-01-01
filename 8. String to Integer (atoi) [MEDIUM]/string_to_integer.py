"""
8. String to Integer (atoi) [MEDIUM]
https://leetcode.com/problems/string-to-integer-atoi

### 1. Question Explanation:
----------------------------
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

### 2. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(1)
"""
class Solution:
    def myAtoi(self, input_str: str) -> int:
        input_str = input_str.strip()  # remove padding spaces

        negative = False  # remove leading + or -
        if input_str and input_str[0] == '-': negative = True
        if input_str and (input_str[0] in ['+', '-']): input_str = input_str[1:]
        if not input_str: return 0

        result, digits = 0, {i for i in '0123456789'}

        for char in input_str:  # record integer upto first non-digit
            if char not in digits: break
            result = result * 10 + int(char)

        if negative: result = -result

        return max(min(result, 2 ** 31 - 1), -2 ** 31)  # keep within 4 byte signed integer bounds
