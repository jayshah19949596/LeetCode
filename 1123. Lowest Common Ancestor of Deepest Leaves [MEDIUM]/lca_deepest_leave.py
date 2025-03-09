"""
===========================
        Approach
===========================
Find the deepest leaves:

Compute the depth of each node.
The deepest leaves will be the ones at the maximum depth.
Find the Lowest Common Ancestor (LCA):

Traverse the tree bottom-up.
If both left and right subtrees have the deepest leaves, the current node is the LCA.
If only one side has the deepest leaves, propagate that side up.

==================
     Solution
==================
We use a recursive function that returns two values:

The depth of the subtree.
The LCA of the deepest leaves in that subtree.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None  # (depth, LCA)
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            else:
                return left_depth + 1, node  # Current node is LCA if depths are equal
        
        return dfs(root)[1]
