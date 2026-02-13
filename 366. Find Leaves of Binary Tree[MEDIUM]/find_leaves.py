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

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.leaves = []     # leaves[i] is ordered list of nodes with height i
        self.height(root)
        return self.leaves

    def height(self, node):
        if not node: return -1
        h = 1 + max(self.height(node.left), self.height(node.right))
        if len(self.leaves) <= h: self.leaves.append([])
        self.leaves[h].append(node.val)
        return h
