"""
125. Valid Palindrome [EASY]
https://leetcode.com/problems/valid-palindrome/

### 1. Question Explanation:
----------------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

#### Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

#### Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

### 2. Solution Explanation:
----------------------------
APPROACH:
Convert to lower case and remove non-alphanumeric characters.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = set(string.ascii_lowercase + string.digits)
        s = [c for c in s.lower() if c in allowed]
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

"""
SPACE OPTIMIZED
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1
        return True