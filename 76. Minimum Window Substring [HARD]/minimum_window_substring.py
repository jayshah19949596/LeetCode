"""
76. Minimum Window Substring [HARD]
https://leetcode.com/problems/minimum-window-substring/

### 1. Question:
----------------------------
Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

### 2. Solution:
----------------------------
Find all indices in S matching the first letter of T and create a list of windows.
For each letter of T, for each window find the next letter of S that matches the letter and extend the window.
If the letter is not found, remove the window. Return the smallest window.

### 3. Complexity Analysis:
----------------------------
Time - O(mn), worst case when all letters are identical means len(S) windows
Space - O(m)
"""
from collections import Counter

# Find all indices in S matching the first letter of T and create a list of windows. 
# For each letter of T, for each window find the next letter of S that matches the letter and extend the window. 
# If the letter is not found, remove the window. Return the smallest window.
# Time - O(mn), worst case when all letters are identical means len(S) windows
# Space - O(m)
class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        start = end = 0
        tc = collections.Counter(t) # original counter
        wc = collections.Counter()  # window counter
        missing = len(t)           # number of characters missing from the window
        best = ""
        
        while end < len(s):
            # go right until we have all characters needed
            while missing != 0 and end<len(s):   
                if s[end] in tc:
                    wc[s[end]] += 1
                    if wc[s[end]] <= tc[s[end]]:
                        missing -= 1
                end += 1
            
            # remove characters from the left until we don't have enough characters anymore
            while missing == 0 and start < len(s):
                while s[start] not in tc: # skip irrelevant characters
                    start += 1
                # compare to and save best solution
                if end-start < len(best) or not best:
                    best = s[start:end]
                wc[s[start]] -= 1
                if wc[s[start]] < tc[s[start]]:
                    missing += 1
                start += 1
        return best
