"""
249. Group Shifted Strings [MEDIUM]
https://leetcode.com/problems/group-shifted-strings/

### 1. Question Explanation:
----------------------------
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of string, group all strings[i] that belong to the same shifting sequence.
You may return the answer in any order.

#### Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

#### Example 2:
Input: strings = ["a"]
Output: [["a"]]



### 2. Solution Explanation:
----------------------------
For all string, keep on shifting the letters till the first character is letter "a".
Group the strings with the sequence where first character is letter "a".
Return the grouped strings as list.

### 3. Complexity Analysis:
----------------------------
Time Complexity - O(N)
Space Complexity - O(N)
"""
from collections import defaultdict
from typing import List


class Solution:
    def shift_string_till_first_char_a(self, original_string):
        char_a, string_list = "a", list(original_string)

        while string_list[0] != char_a:

            for i, char in enumerate(string_list):
                if ord(char) == 122:  # if ascii value is "z" then make it "a"
                    string_list[i] = char_a
                else:
                    string_list[i] = chr(ord(char)+1)

        return "".join(string_list)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        self.grouping = defaultdict(list)
        for original_string in strings:
            sequence_starting_with_a = self.shift_string_till_first_char_a(original_string)
            self.grouping[sequence_starting_with_a].append(original_string)
        return [self.grouping[key] for key in self.grouping]