"""
408. Valid Word Abbreviation [EASY]
https://leetcode.com/problems/valid-word-abbreviation/

### 1. Question Explanation:
----------------------------
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):
"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)

The following are not valid abbreviations:
"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

#### Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

#### Example 2:
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

### 2. Solution Explanation:
----------------------------
- Use two pointer approach.
- One pointer to iterate "word" and other pointer to iterate "abbr".
- Increment both pointers if letters of "word" and "abbr" match
- If letter of "abbr" is integer then skip increment the "word" pointer by the "abbr" integer
- If letters of "word" and "abbr" do not match then return False

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(1)
"""


"""
https://leetcode.com/problems/valid-word-abbreviation/

### 1. Question Explanation:
----------------------------
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):
"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)

The following are not valid abbreviations:
"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

#### Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

#### Example 2:
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

### 2. Solution Explanation:
----------------------------
- Use two pointer approach.
- One pointer to iterate "word" and other pointer to iterate "abbr".
- Increment both pointers if letters of "word" and "abbr" match
- If letter of "abbr" is integer then skip increment the "word" pointer by the "abbr" integer
- If letters of "word" and "abbr" do not match then return False

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = abbr_idx = 0
        while word_idx < len(word) and abbr_idx < len(abbr):
            if word[word_idx] == abbr[abbr_idx]:
                word_idx += 1
                abbr_idx += 1
            elif abbr[abbr_idx].isnumeric() and abbr[abbr_idx] != "0":
                abbr_num = 0
                while abbr_idx < len(abbr) and abbr[abbr_idx].isnumeric():
                    abbr_num = abbr_num*10 + int(abbr[abbr_idx])
                    abbr_idx += 1
                word_idx += abbr_num
            else:  # word[word_idx] ! = abbr[abbr_idx] and abbreviation not satisfied
                return False
        return word_idx == len(word) and abbr_idx == len(abbr)