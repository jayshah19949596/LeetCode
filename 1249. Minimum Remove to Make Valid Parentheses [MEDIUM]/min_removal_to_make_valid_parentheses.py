"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

### 1. Question Explanation:
----------------------------
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses
string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with
B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

### 2. Solution Explanation:
----------------------------
Iterate along s, adding opening brackets to a list.
If we see a closing bracket without any opening bracket, it must be removed.
If we see a closing bracket with unmatched opening
brackets, discard the matching opening bracket.
Finally, discard any unmatched opening brackets before
reconstructing s without discarded indices.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution(object):
    def minRemoveToMakeValid(self, s: str) -> str:
        opening, removals = [], set([])

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                opening.append(i)
            elif char == ")":
                if opening: opening.pop()
                else: removals.add(i)

        removals.update(opening)
        results = []

        for i in range(len(s)):
            if i not in removals: results.append(s[i])
        return "".join(results)