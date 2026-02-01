"""
242. Valid Anagram [EASY]
https://leetcode.com/problems/valid-anagram

### 1. Question:
----------------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

#### Example 2:
Input: s = "rat", t = "car"
Output: false
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return self.using_sorting(s, t)
        return self.using_hashmap(s, t)

    def using_hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_zeros = 0
        for char in t:
            if char in count_s and count_s[char] > 0:
                count_s[char] -= 1
                if count_s[char] == 0: count_zeros += 1
                continue
            return False
        return count_zeros == len(count_s)

    def using_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
