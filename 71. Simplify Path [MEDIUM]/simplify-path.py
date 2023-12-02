"""
https://leetcode.com/problems/simplify-path/

### 1. Question Explanation:
----------------------------
Given an absolute path for a file (Unix-style), simplify it.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

### 2. Solution Explanation:
----------------------------
Create result stack. Go up a level if '..'. Stay at same level if '.'.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        results = []

        for i, path_element in enumerate(path_list):
            if path_element == "" or path_element == ".":
                continue
            elif path_element == "..":
                if results: results.pop()
            else:
                results.append(path_element)

        return "/" + "/".join(results)