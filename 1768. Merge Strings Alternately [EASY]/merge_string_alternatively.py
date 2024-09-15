"""
1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately

### 1. Question Explanation:
----------------------------
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


#### Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

### 2. Solution Explanation:
----------------------------
???

### 3. Complexity Analysis:
----------------------------
Time - O(len(word1) + len(word2))
Space - O(1)
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        results = []
        n = max(len(word1), len(word2))

        for i in range(n):
            if i < len(word1): results.append(word1[i])
            if i < len(word2): results.append(word2[i])

        return "".join(results)