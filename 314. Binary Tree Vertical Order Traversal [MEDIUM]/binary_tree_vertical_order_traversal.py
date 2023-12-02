"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal

### 1. Question Explanation:
----------------------------
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

#### Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

### 2. Solution Explanation:
----------------------------
Use columnar index to identify which column does the nodes are in.
Use BFS to traverse the tree and identify the columnar index of the node.
Display the results.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N), where N is the number of nodes in the tree.
"""
from typing import List
from typing import Optional
from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        col_mapping = defaultdict(list)
        dequeue = deque([[root, 0]])
        min_col, max_col = float("inf"), -float("inf")

        while dequeue:
            node, col_idx = dequeue.popleft()
            col_mapping[col_idx].append(node.val)
            min_col, max_col = min(min_col, col_idx), max(max_col, col_idx)
            if node.left: dequeue.append([node.left, col_idx - 1])
            if node.right: dequeue.append([node.right, col_idx + 1])

        results = [col_mapping[i] for i in range(min_col, max_col + 1)]
        return results
