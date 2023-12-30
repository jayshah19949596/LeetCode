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

from collections import defaultdict


"""
APPROACH-1: DFS with Memoization and Pruning
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.removals_to_expression_map = defaultdict(set)
        self.memo = defaultdict(int)
        min_removal = self.recurse(s, 0, [], 0, [float("inf")])
        return list(self.removals_to_expression_map[min_removal])

    def isValid(self, s):
        balance = 0
        for i in range(len(s)):
            if s[i] == "(": balance += 1
            elif s[i] == ")":
                if balance>0:balance -= 1
                else: return False
        return balance == 0

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

        keep_current_character_ans = self.recurse(s, cur_idx + 1, new_s + [s[cur_idx]], removals, global_min_removal)
        remove_parenthesis_ans = float("inf")
        if s[cur_idx] in ["(", ")"]:
            remove_parenthesis_ans = self.recurse(s, cur_idx + 1, new_s, removals + 1, global_min_removal)

        self.memo[new_s_string] = min(keep_current_character_ans, remove_parenthesis_ans)
        return self.memo[new_s_string]


"""
APPROACH-2: Additional pruning of operations
"""
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        removals_map = defaultdict(set)
        min_removals = float("inf")
        memo = {}
        def is_valid(string):
            balance = 0
            for char in string:
                if char == "(":
                    balance += 1
                elif char == ")":
                    if balance>0:
                        balance -= 1
                    else:
                        return False
            return balance == 0

        def dfs(idx, inter_string, removals, balance):
            nonlocal removals_map, min_removals, memo, s

            if len(s)-balance < balance:  # Pruning the dfs search by checking if we have characters remaining to bring balance to 0
                return float("inf")

            if (idx, inter_string) in memo:
                return memo[(idx, inter_string)]

            if removals>min_removals:  # Pruning the dfs search if removals is greater than min_removals
                return float("inf")

            if idx == len(s):
                if balance == 0 and is_valid(inter_string):  # Pruning is_valid operations if balance != 0
                    removals_map[removals].add(inter_string)
                    min_removals = min(min_removals, removals)
                    return min_removals
                return float("inf")

            new_balance = balance
            removal_ans = float("inf")
            if s[idx] == "(":
                new_balance += 1
                removal_ans = dfs(idx+1, inter_string, removals+1, balance)
            elif s[idx] == ")":
                new_balance -= 1
                removal_ans = dfs(idx+1, inter_string, removals+1, balance)

            keep_ans = dfs(idx+1, inter_string+s[idx], removals, new_balance)
            memo[(idx, inter_string)] = min(keep_ans, removal_ans)
            return memo[(idx, inter_string)]

        dfs(0, "", 0, 0)
        return list(removals_map[min_removals])