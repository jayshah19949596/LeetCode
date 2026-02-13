# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Given a binary tree, collect a tree's nodes as if
# you were doing this: Collect and remove all leaves,
# repeat until the tree is empty.

# Bottom-up preorder traversal to find height
# of each node (1 + max height of children).
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []

        def dfs(node):
            if not node: return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            h = 1 + max(left_height, right_height)

            if len(leaves) <= h: leaves.append([])
            leaves[h].append(node.val) 

            return h

        dfs(root)
        return leaves
