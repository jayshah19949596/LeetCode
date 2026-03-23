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
        # Stack will store [previous_total, previous_sign]
        stack = []
        num, sign = 0, 1
        ans = 0
        s = s + "+" # We add a '+' at the end to "flush" the final number into the total
        
        for char in s:
            if char.isdigit():
                # Correctly build multi-digit numbers (e.g., "42")
                num = num * 10 + int(char)
            
            elif char in "+-":
                # Finalize the current number before moving to the next sign
                ans += sign * num
                # Update sign for the NEXT number
                sign = 1 if char == "+" else -1
                num = 0
                
            elif char == "(":
                # Pushing a nested list: [current_total, current_sign]
                stack.append([ans, sign])
                # Reset for the expression inside the parentheses
                ans, sign = 0, 1
                
            elif char == ")":
                # Finalize the last number inside the parentheses
                ans += sign * num
                num = 0
                
                # Retrieve the nested list [prev_ans, prev_sign]
                prev_ans, prev_sign = stack.pop()
                
                # Result = (Inside_Result * sign_before_paren) + ans_before_paren
                ans = prev_ans + (prev_sign * ans)
                
        return ans
        
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
