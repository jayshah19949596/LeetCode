"""
1371. Find the Longest Substring Containing Vowels in Even Counts
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts

BRUTE FORCE SOLUTION
--------------------
1. Iterate through all possible substrings using two nested loops.
2. For each substring, count the occurrences of each vowel.
3. Check if all vowels have even counts.
4. Update the maximum length if the condition is met.

TIME COMPLEXITY: O(n^3)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_length = 0

        # Function to check if all vowels have even counts
        def all_vowels_even(counts):
            return all(count % 2 == 0 for count in counts.values())

        # Iterate through all possible substrings
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # Count vowels in the current substring
                vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
                for char in substring:
                    if char in vowel_counts:
                        vowel_counts[char] += 1

                # Check if all vowels have even counts
                if all_vowels_even(vowel_counts):
                    max_length = max(max_length, end - start)

        return max_length