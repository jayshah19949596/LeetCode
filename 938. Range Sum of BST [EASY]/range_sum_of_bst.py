"""
https://leetcode.com/problems/range-sum-of-bst/

### 1. Question Explanation:
----------------------------
Given the root node of a binary search tree, return
the sum of values of all nodes with value between
L and R (inclusive).
The binary search tree is guaranteed to have unique values.

### 2. Solution Explanation:
----------------------------
If the node value is more than R then recurse left only because
all node values in right subtree are even greater.
If the node value is less than L then recurse right only
because all node values in left subtree are even lower.
Else return the sum of the node value (since it is in the
target range) plus the results from the left and right
subtrees.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # return self.recursive(root, L, R)
        return self.iterative(root, L, R)

    def recursive(self, node, low, high):
        if not node: return 0
        if node.val > high: return self.recursive(node.left, low, high)
        if node.val < low: return self.recursive(node.right, low, high)

        return node.val + self.recursive(node.left, low, high) + self.recursive(node.right, low, high)

    def iterative(self, root, low, high):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans