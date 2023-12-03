"""
https://leetcode.com/problems/remove-invalid-parentheses

### 1. Question Explanation:
----------------------------
Given a string "s" that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of "unique strings" that are valid with the minimum number of removals. You may return the answer in "any order".

#### Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

#### Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

#### Example 3:
Input: s = ")("
Output: [""]

### 2. Solution Explanation:
----------------------------
For every bracket we have two choices:
1. Either it can be considered a part of the final expression OR
2. It can be ignored i.e. we can delete it from our final expression.
Do the above operations recursively and calculate the number of removals

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(2^N).
Space Complexity: O(N).
"""
from collections import defaultdict
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.removals_to_expression_map = defaultdict(set)
        self.memo = defaultdict(int)
        min_removal = self.recurse(s, 0, [], 0, [float("inf")])
        return list(self.removals_to_expression_map[min_removal])

    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack

    def recurse(self, s, cur_idx, new_s, removals, global_min_removal):
        new_s_string = "".join(new_s)

        if new_s_string in self.memo:
            return self.memo[new_s_string]

        if removals > global_min_removal[0]:
            return float("inf")

        if cur_idx == len(s):
            if self.isValid(new_s):
                global_min_removal[0] = min(global_min_removal[0], removals)
                self.removals_to_expression_map[removals].add(new_s_string)
                return removals
            else:
                return float("inf")

        keep_removals_ans = self.recurse(s, cur_idx + 1, new_s + [s[cur_idx]], removals, global_min_removal)
        remove_removals_ans = float("inf")
        if s[cur_idx] in ["(", ")"]:
            remove_removals_ans = self.recurse(s, cur_idx + 1, new_s, removals + 1, global_min_removal)

        self.memo[new_s_string] = min(keep_removals_ans, remove_removals_ans)
        return self.memo[new_s_string]