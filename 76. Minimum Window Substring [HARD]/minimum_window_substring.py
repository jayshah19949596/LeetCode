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
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t) # what we must have
        window = Counter() # what we currently have
        missing = len(t) # how many required characters are still missing

        left = 0
        res = ""

        for right, ch in enumerate(s):
            window[ch] += 1
            if window[ch] <= need[ch]:
                missing -= 1

            while missing == 0:
                if not res or right - left + 1 < len(res):
                    res = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] < need[left_char]:
                    missing += 1
                left += 1
        
        return res
