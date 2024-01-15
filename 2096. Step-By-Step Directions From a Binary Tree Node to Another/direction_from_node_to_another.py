"""
2096. Step-By-Step Directions From a Binary Tree Node to Another [MEDIUM]
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def find_lca(root, p, q):
            # From : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/
            if not root or p == root.val or q == root.val:  # base cases
                return root

            left_lca = find_lca(root.left, p, q)
            right_lca = find_lca(root.right, p, q)

            if left_lca and right_lca:
                return root
            elif left_lca:
                return left_lca
            else:
                return right_lca

        root = find_lca(root, startValue, destValue)  # only this sub-tree matters
        path_start = path_dest = ""
        found_start = found_dest = False
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                path_start = path
                found_start = True
            if node.val == destValue:
                path_dest = path
                found_dest = True
            if found_start and found_dest: break
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U" * len(path_start) + path_dest
