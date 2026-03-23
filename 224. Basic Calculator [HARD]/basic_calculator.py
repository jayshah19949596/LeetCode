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
        num, sign = 0, 1 # 1 means positive, -1 means negative  
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
     
