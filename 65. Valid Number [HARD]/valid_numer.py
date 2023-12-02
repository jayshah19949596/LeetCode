"""
https://leetcode.com/problems/valid-number

### 1. Question Explanation:
----------------------------
A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
   1. One or more digits, followed by a dot '.'.
   2. One or more digits, followed by a dot '.', followed by one or more digits.
   3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string "s", return "true" if "s" is a valid number.

### 2. Solution Explanation:
----------------------------
Rules

1. DIGITS: First of all, there must always be at least one digit in the input for it to form a valid number. Let's use a variable seenDigit to indicate whether we have seen a digit yet.
2. SIGNS: If a sign is present, it must be the first character in a decimal number or integer. In a valid number, there are two possible locations for these signs - at the front of the number, or right after an exponent ("e" or "E") e.g., -63e+7. Therefore, if we see a sign, and it is not the first character of the input, and does not come immediately after an exponent ("e" or "E"), then we know the number is not valid.
3. EXPONENTS ("e" or "E"): There cannot be more than one exponent in a valid number, so we will use a variable seenExponent to indicate whether we have already seen an exponent.
An exponent must appear after a decimal number or an integer. This means if we see an exponent, we must have already seen a digit.
4. DOTS: There cannot be more than one dot in a valid number, since only integers are allowed after an exponent, so there cannot be more than one decimal number. We will use a variable seenDot to indicate whether we have seen a dot.
If we see a dot appear after an exponent, the number is not valid, because integers cannot have dots.
Anything else
5. ELSE: Seeing anything else instantly invalidates the input.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(1)
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_dot = seen_exponent = False
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ["+", "-"]:
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
            elif char in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif char == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False                
        return seen_digit