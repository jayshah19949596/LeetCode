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
"""

"""
============================
## APPROACH 1: Using Stack

### 1. Solution Explanation:
----------------------------
Iterate along s, adding opening brackets to a list.
If we see a closing bracket without any opening bracket, it must be removed.
If we see a closing bracket with unmatched opening
brackets, discard the matching opening bracket.
Finally, discard any unmatched opening brackets before
reconstructing s without discarded indices.

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
============================
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
"""
============================
# APPROACH 2: Two Pass with reverse
============================

### 1. Solution Explanation:
----------------------------
We can use the same algorithm to remove the invalid "(" in Approach-1.
We just need to look at the string in reverse. We do this by swapping the "(" and ")" for each other,
and reversing the order of all characters in the string
So then we can remove those characters,
and undo the reverse operation by reversing all characters and swapping "(" and ")" again,
and we have the answer

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(ip_string, open_symbol, close_symbol):
            string_list = []
            balance = 0
            for char in ip_string:
                if char == open_symbol:
                    balance += 1
                if char == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                string_list.append(char)
            return "".join(string_list)

        # Note that s[::-1] gets the reverse of s.
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]

"""
============================
# APPROACH 3: Shortened Two Pass
============================

### 1. Solution Explanation:
----------------------------
In order to avoid iterating backwards (which adds needless complexity to the algorithm),
we also keep track of how many "(" are in the string in the first pass.
This way, we can calculate how many "(" we are keeping,
and count these down as we iterate through the string on the second pass.
Then once we've kept enough, we can start dropping them.

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
         # Pass 1: Remove all invalid ")"
        first_pass_chars = []
        balance = open_seen = 0
        for char in s:
            if char == "(":
                balance += 1
                open_seen += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(char)

        # Pass 2: Remove the rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for char in first_pass_chars:
            if char == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(char)

        return "".join(result)
