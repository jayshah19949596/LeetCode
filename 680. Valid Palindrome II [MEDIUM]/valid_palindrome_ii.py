"""
https://leetcode.com/problems/valid-palindrome-ii

### 1. Question Explanation:
----------------------------
Given a string "s", return "true" if the "s" can be palindrome after deleting at most one character from it.

#### Example 1:
Input: s = "aba"
Output: true

#### Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

#### Example 3:
Input: s = "abc"
Output: false

### 2. Solution Explanation:
----------------------------
APPROACH: Two Pointers
Initialize one pointer at the start of the string and one at the end.
Compare the characters at these pointers - if they're different, the string can't be a palindrome. If they're the same, then move the pointers towards each other.
Continue until there is a mismatch (signifying the string is not a palindrome) or until the pointers meet each other (which would mean the string is a palindrome).


### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution:
    def check_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                # delete the character at jth index or delete the character at ith index
                return self.check_palindrome(s, i, j - 1) or self.check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        return True
