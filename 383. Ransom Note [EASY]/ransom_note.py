"""
383. Ransom Note [Easy]
https://leetcode.com/problems/ransom-note

### 1. Question:
---------------------------
Given two strings "ransomNote" and "magazine".
Return true if "ransomNote" can be constructed by using the letters from "magazine" and false otherwise.
Each letter in "magazine" can only be used once in "ransomNote".

### Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

### Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

### Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

### 2. Complexity:
---------------------------
Time: O(N)
Space: O(N)
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        total_char_seen = 0
        for char in magazine:
            if char in count_ransom and count_ransom[char] > 0:
                count_ransom[char] -= 1
                if count_ransom[char] == 0:
                    total_char_seen += 1
        return total_char_seen == len(count_ransom)
