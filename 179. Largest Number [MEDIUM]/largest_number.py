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
    def largestNumber(self, nums: List[int]) -> str:
        def lambda_func(a):
            # print(a*10)
            return a*10
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: lambda_func(a), reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)
