"""
2330. Valid Palindrome IV [MEDIUM]

https://leetcode.com/problems/valid-palindrome-iv

### 1. Question Explanation:
----------------------------
You are given a 0-indexed string s consisting of only lowercase English letters. In one operation, you can change any character of s to any other character.

Return true if you can make s a palindrome after performing exactly one or two operations, or return false otherwise.


### 2. Solution Explanation:
----------------------------
l and r are pointers to the left and right ends of the string, respectively.
no_op counts the number of operations (character changes) needed.
If the characters at positions l and r don't match, increment no_op.
If no_op reaches 3, return False because more than two changes would be needed.
If the loop completes without return True, it means the string can be made into a palindrome with at most two changes.

### 3. Complexity Analysis:
----------------------------
Time complexity: O(N).
Space complexity: O(1).
"""
class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        no_op = 0
        while l<r:
            if s[l] != s[r]:
                no_op += 1
                if no_op == 3:
                    return False
            l, r = l+1, r-1
        return True