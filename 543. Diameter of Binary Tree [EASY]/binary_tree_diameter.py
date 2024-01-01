"""
543. Diameter of Binary Tree [EASY]
https://leetcode.com/problems/diameter-of-binary-tree/

### 1. Question Explanation:
----------------------------
Given a binary tree, you need to compute
the length of the diameter of the tree.
The diameter of a binary tree is the length of the
longest path between any two nodes in a tree.
This path may or may not pass through the root.

### 2. Solution Explanation:
----------------------------
Bottom up recursion. The longest path passing with a node
as root is the longest downwards left path + longest downwards right path.
If there is no child on right or left then the longest path on that side is zero.
Else longest path is 1 + longest of left and right paths down from child.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(1)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_edge_count = dfs(node.left)
            right_edge_count = dfs(node.right)
            max_diameter = max(max_diameter, left_edge_count + right_edge_count)
            return 1 + max(left_edge_count, right_edge_count)

        dfs(root)
        return max_diameter
