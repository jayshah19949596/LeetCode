"""
938. Range Sum of BST [EASY]
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
        """ans = [0]
        self.top_down_recurse(root, low, high, ans)
        return ans[0]"""
        # return self.bottom_up_recurse(root, low, high)
        return self.iterative(root, low, high)

    def bottom_up_recurse(self, node, low, high):
        if not node: return 0
        if node.val > high:
            return self.bottom_up_recurse(node.left, low, high)
        if node.val < low:
            return self.bottom_up_recurse(node.right, low, high)
        return node.val + self.bottom_up_recurse(node.left, low, high) + self.bottom_up_recurse(node.right, low, high)

    def top_down_recurse(self, node, low, high, ans):
        if not node: return
        elif low <= node.val <= high:
            self.top_down_recurse(node.left, low, high, ans)
            self.top_down_recurse(node.right, low, high, ans)
            ans[0] = ans[0] + node.val
        elif node.val < low: # OutOfBound Condition
            self.top_down_recurse(node.right, low, high, ans)
        elif node.val > high:
            self.top_down_recurse(node.left, low, high, ans)

    def iterative(self, root, low, high):
        stack, ans = [root], 0
        while stack:
            node = stack.pop()
            if not node: continue
            elif low <= node.val <= high:
                ans += node.val
                stack.append(node.left)
                stack.append(node.right)
            elif node.val < low: # OutOfBound Condition
                stack.append(node.right)
            elif node.val > high: # OutOfBound Condition
                stack.append(node.left)
        return ans