"""
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

### 1. Question Explanation:
----------------------------
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

#### Example 1:
Input: s = "1 + 1"
Output: 2

#### Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left, with result, sign, operand
                res += sign * operand
                # Save the recently encountered '+' sign
                sign = 1
                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis 
                # Its result is multiplied with sign on top of stack as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # As stack.pop() is the result calculated before this parenthesis (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand
                
                operand = 0  # Reset the operand

        return res + sign * operand
