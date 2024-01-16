"""
742. Closest Leaf in a Binary Tree [MEDIUM]
https://leetcode.com/problems/closest-leaf-in-a-binary-tree

### 1. Question:
----------------------------
Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.
Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

### Complexity:
---------------------------
Time: O(N)
Space: O(H): Height of the tree,  stored in "path" variable.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:

        def find_path_dfs(node, path):
            if not node: return None
            if node.val == k:
                path.append(node)
                return node
            lft_return_node = find_path_dfs(node.left, path)
            ryt_return_node = find_path_dfs(node.right, path)
            if lft_return_node or ryt_return_node:
                path.append(node)
                return node
            return

        def dfs_closest_leaf(node, dist, blocker):
            nonlocal closes_dist_leaf
            if node is None or node == blocker or dist >= closes_dist_leaf[0]: return
            if node.left is None and node.right is None:
                closes_dist, closest_leaf = closes_dist_leaf
                if closes_dist > dist: closes_dist_leaf = (dist, node)
                return
            dfs_closest_leaf(node.left, dist + 1, blocker)
            dfs_closest_leaf(node.right, dist + 1, blocker)

        root_to_k_path = []
        closes_dist_leaf = (float(inf), None)
        find_path_dfs(root, root_to_k_path)
        for i, node in enumerate(root_to_k_path):
            if i == 0:
                blocker = None
            else:
                blocker = root_to_k_path[i - 1]
            dfs_closest_leaf(node, i, blocker)
        return closes_dist_leaf[1].val