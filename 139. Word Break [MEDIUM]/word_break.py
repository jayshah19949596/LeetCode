"""
139. Word Break [MEDIUM]
https://leetcode.com/problems/word-break

### 1. Question:
----------------------------
Given a string "s" and a dictionary of strings "wordDict", return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

#### Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

#### Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

#### Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.dynamic_programming(s, wordDict)
        return self.recurse(s, wordDict)

    def recurse_topdown(self, s, wordDict):
        """
        ### Explanation:
        For all the words in dictionary that are prefix of string, recursively call function with substring removing the prefix from string.
        Meanwhile, store the overlapping sub-problems for each substring to avoid the computation of the sub-problem again.

        ### Complexity Analysis
        Given "n" as the length of "s", "m" as the length of "wordDict", and "k" as the average length of the words in "wordDict"

        Time complexity: O(n^3):
        There are O(n) nodes. Because of memo, we never visit a node more than once.
        At each node, we iterate over the nodes in front of the current node, of which there are O(n).
        For each node end, we create a substring, which also costs O(n)
        Therefore, handling a node costs O(n^2), so the DFS could cost up to O(n^3):

        Space Complexity: O(n):
        We use O(n) space for recursion stack and memo.
        """
        if len(s) == 0:
            return True

        if s in self.memo:
            return self.memo[s]

        for word in wordDict:
            if s.startswith(word) and self.recurse(s[len(word):], wordDict):
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False

    def dynamic_programming(self, s, wordDict):
        """
        Time complexity: O(n*m*k)
        Space Complexity: O(n)
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

