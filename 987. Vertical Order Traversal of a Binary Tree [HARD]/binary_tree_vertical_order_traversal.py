"""
987. Vertical Order Traversal of a Binary Tree [HARD]
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

### 1. Question Explanation:
----------------------------
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively.
The root of the tree is at (0, 0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column.
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.

### 2. Solution Explanation:
----------------------------
Use columnar index to identify which column does the nodes are in.
Use DFS to traverse the tree and identify the columnar index of the node.
Display the results.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N), where N is the number of nodes in the tree.
"""
from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = root
        number2node = defaultdict(list)
        stack = [[node, 0, 0]]
        max_col, min_col = -float("inf"), float("inf")

        while stack:
            cur, row, col = stack.pop()
            max_col, min_col = max(max_col, col), min(min_col, col)
            number2node[col].append([cur.val, row])
            if cur.left: stack.append([cur.left, row + 1, col - 1])
            if cur.right: stack.append([cur.right, row + 1, col + 1])

        results = []
        for i in range(min_col, max_col + 1):
            sorted_results = sorted(number2node[i], key=lambda x: (x[1], x[0]))
            intermediate_res = []
            for element in sorted_results:
                intermediate_res.append(element[0])
            results.append(intermediate_res)
        return results
