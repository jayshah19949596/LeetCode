"""
129. Sum Root to Leaf Numbers [MEDIUM]
https://leetcode.com/problems/sum-root-to-leaf-numbers

### 1. Question Explanation:
----------------------------
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

### 2. Solution Explanation:
----------------------------
APPROACH:
Traverse through each node in the tree and stor the digit in a variable.
When a leaf node is encountered add the digit storing variable to overall answer

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # return self.recurse_dfs(root, 0)
        return self.iterative_dfs(root)

    def recurse_dfs(self, node, num_so_far):
        if not node: return 0
        if not node.left and not node.right:
            return num_so_far*10+node.val
        left_summ = self.recurse_dfs(node.left, num_so_far*10+node.val)
        right_summ = self.recurse_dfs(node.right, num_so_far*10+node.val)
        return left_summ+right_summ

    def iterative_dfs(self, node):
        if not node: return 0
        stack, answer = [[node, 0]], 0
        while stack:
            cur_node, cur_num_so_far = stack.pop()
            if not cur_node.left and not cur_node.right:
                answer+=cur_num_so_far*10+cur_node.val
            else:
                if cur_node.left: stack.append([cur_node.left, cur_num_so_far*10+cur_node.val])
                if cur_node.right: stack.append([cur_node.right, cur_num_so_far*10+cur_node.val])
        return answer
