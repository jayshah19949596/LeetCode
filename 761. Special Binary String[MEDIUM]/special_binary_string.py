# https://leetcode.com/problems/special-binary-string/
# Special binary strings are binary strings with the following two properties:
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# Given a special string S, a move consists of choosing two
# consecutive, non-empty, special substrings of S, and
# swapping them. (Two strings are consecutive if the last character
# of the first string is exactly one index before the
# first character of the second string.)
# At the end of any number of moves, what is the lexicographically
# largest resulting string possible?

# Create a list of all optimal special strings,
# sort in order of most starting 1s and join.
# To create an optimal special string, iterate over S finding
# the point there the next balance of 1s minus 0s falls to
# zero. Remove the leading 1 and trailing 0 and recurse on
# the middle part. Middle part is a special string because
# A) it has an equal number of 1s and 0s and B) if a prefix
# of the middle has one less 1 and 0, it will already be
# processed, so every prefix of middle has as many 1s
# as 0s, which is the definition of a special string.
# Time - O(n**2)
# Space - O(n)


"""
If you replace 1 with '(' and 0 with ')', these are exactly the rules for Valid Parentheses.

1100 -> (()) (Special)
1010 -> ()() (Special)
0101 -> )()( (NOT Special)

The Goal: Make the string lexicographically largest by swapping adjacent special substrings. 
In parentheses terms, we want to move the "heaviest" or "most deeply nested" structures to the front.

2. The Recursive Strategy
Any "Special" string can be broken down into multiple Atomic Special Substrings.
An atomic string is one that cannot be split into two special strings 
(e.g., 1100 is atomic, but 1010 is two atomic 10s put together).

The Algorithm:
1. Split the string into its independent "Special" components.
2. Recursively simplify the "inside" of each component.
3. Since every atomic special string must start with 1 and end with 0, the "inside" is s[1:-1].
4. Sort these simplified components in descending order (to make the string lexicographically largest).
5. Rejoin them.
"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s: return ""

        specials = []
        balance = start = 0
        for end, char in enumerate(s):
            if char == "1": balance += 1
            else: balance -= 1

            if balance == 0:
                nxt_innter_str = s[start+1: end]
                lexico_sorted = self.makeLargestSpecial(nxt_innter_str)
                specials.append("1" + lexico_sorted + "0")
                start = end+1

        specials.sort(reverse=True)
        return "".join(specials)
