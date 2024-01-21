"""
722. Remove Comments [MEDIUM]
https://leetcode.com/problems/remove-comments

### 1. Question:
----------------------------
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code.
This represents the result of splitting the original source code string by the newline character '\n'.
In C++, there are two types of comments, line comments, and block comments.
1] The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
2] The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others.
For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.


#### Example 1:
Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
Explanation: The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
The line by line output code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

#### Example 2:
Input: source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
"""
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result = []
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        in_block = True
                        i += 1
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        break
                    else:
                        current_line.append(line[i])
                else:
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block = False
                        i += 1

                i += 1

            if current_line and not in_block:
                result.append("".join(current_line))
                current_line = []

        return result
