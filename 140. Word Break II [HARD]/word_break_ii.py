"""
https://leetcode.com/problems/word-break-ii/

### 1. Question Explanation:
----------------------------
Given a string "s" and a dictionary of strings "wordDict", add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.


#### Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

#### Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

#### Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N^2+2^N +W)
Where N be the length of the input string and W be the number of words in the dictionary.

Space Complexity: O(2^N*N+W)
"""
from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)
        # break the input string into lists of words list
        self.recurse_topdown(s, wordDict, memo)
        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]

    # @lru_cache(maxsize=None)    # alternative memoization solution
    def recurse_topdown(self, s, word_dict, memo):
        """ return list of word lists """
        if len(s) == 0: return [[]]  # list of empty list

        if s in memo: return memo[s]

        for word in word_dict:
            if s.startswith(word):
                sub_sentences = self.recurse_topdown(s[len(word):], word_dict, memo)
                for sub_sentence in sub_sentences:
                    memo[s].append([word] + sub_sentence)

        return memo[s]