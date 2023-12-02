"""
https://leetcode.com/problems/basic-calculator-ii/

### 1. Question Explanation:
----------------------------
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative
integers, +, -, *, / operators and empty spaces.
The integer division should truncate toward zero.
You may assume that the given expression is always valid.

#### Example 1:
Input: s = "3+2*2"
Output: 7

#### Example 2:
Input: s = " 3/2 "
Output: 1

#### Example 3:
Input: s = " 3+5 / 2 "
Output: 5

### 2. Solution Explanation:
----------------------------
Create a stack of partial results to be summed to get
the full result.  Iterate over s.  When c is a digit
increase the current integer num.  When c is an operator
or at end of string, apply the previous operator
to num.  For '*' and '/' this uses the previous integer on the stack.

### 3. Complexity Analysis:
----------------------------
Time Complexity - O(N)
Space Complexity - O(N)
"""


class Solution(object):
    def calculate(self, s: str) -> int:
        stack, num, op = [], 0, "+"

        for i, c in enumerate(s):

            if c.isdigit():                 # build num
                num = num*10 + int(c)

            if (not c.isdigit() and c != ' ') or i == len(s)-1:    # c is an operator or end of string
                if op == '+':               # use previous operator op
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:   # op == '/'
                    left = stack.pop()
                    stack.append(int(left/num))

                num = 0     # num has been used so reset
                op = c

        return sum(stack)
