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
"""


class Solution:
    """
    ### Approach 1: Stack
    Create a stack of partial results to be summed to get
    the full result.  Iterate over s.  When c is a digit
    increase the current integer num.  When c is an operator
    or at end of string, apply the previous operator
    to num.  For '*' and '/' this uses the previous integer on the stack.

    ### Complexity Analysis:
    ----------------------------
    Time Complexity - O(N)
    Space Complexity - O(N)
    """
    def calculate(self, s: str) -> int:
        stack, op = [], "+"
        num = i = 0
        operators = set(["+", "-", "*", "/"])

        while i<len(s):

            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            if i >= len(s)-1 or s[i] in operators:
                if op == "+": stack.append(num)
                elif op == "-": stack.append(-num)
                elif op == "*": stack.append(stack.pop()*num)
                elif op == "/": stack.append(int(stack.pop()/num))
                if i<len(s): op, num = s[i], 0
            i += 1

        return sum(stack)


class Solution:
    """
    ### Approach 2: Optimised Approach without the stack
    - Instead of using a stack, we use a variable lastNumber to track the value of the last evaluated expression.
    - If the operation is Addition (+) or Subtraction (-), add the lastNumber to the result instead of pushing it to the stack.
    - The currentNumber would be updated to lastNumber for the next iteration.
    - If the operation is Multiplication (*) or Division (/), we must evaluate the expression lastNumber * currentNumber and update the lastNumber with the result of the expression.
    - This would be added to the result after the entire string is scanned.

    ### Complexity Analysis:
    ----------------------------
    Time Complexity - O(N)
    Space Complexity - O(1)
    """
   def calculate(self, s: str) -> int:
        i = tot_sum = prv_num = cur_num = 0
        op = "+"
        operators = set(["+", "-", "*", "/"])

        while i < len(s):

            while i < len(s) and s[i].isdigit():  # build num
                cur_num = cur_num * 10 + int(s[i])
                i += 1

            if i >= len(s)-1 or s[i] in operators:
                if op == "+":
                    tot_sum += prv_num
                    prv_num = cur_num
                elif op == "-":
                    tot_sum += prv_num
                    prv_num = -cur_num
                elif op == "*": prv_num = prv_num * cur_num
                else: prv_num = int(prv_num / cur_num)

                if i<len(s): op, cur_num = s[i], 0
                
            i += 1

        return tot_sum+prv_num
