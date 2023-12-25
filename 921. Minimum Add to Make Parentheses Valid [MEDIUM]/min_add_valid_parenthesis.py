"""
921. Minimum Add to Make Parentheses Valid [Medium]
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

### 1. Question Explanation:
-----------------
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

#### Example 1:
Input: s = "())"
Output: 1

#### Example 2:
Input: s = "((("
Output: 3

### 2. Solution Explanation:
----------------------------
Keep track of the balance of the string: the number of '(''s minus the number of ')''s.
A string is valid if its balance is 0, plus every prefix has non-negative balance

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(1)

"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        insertions = 0
        for idx, char in enumerate(s):
            if char == "(":
                balance += 1
            elif char == ")":
                if balance>0:
                    balance -= 1
                else:
                    insertions += 1
        return insertions+balance
