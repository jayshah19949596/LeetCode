"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find path from child node to root node.
        Where ever is the last common ancestor in path from child node to root node for both children is the LCA

        Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(N) - Where N is number of node in the tree
        """
        return self.findLCA(root, p, q)  # SOLUTION ===> 1

    def bottom_up_find_path(self, root, path, k):
        if root is None: return False

        if root.val == k.val:
            path.append(root)
            return True

        if self.bottom_up_find_path(root.left, path, k) or self.bottom_up_find_path(root.right, path, k):
            path.append(root)
            return True

        return False

    def findLCA(self, root, n1, n2):
        path1, path2 = [], []

        if not self.bottom_up_find_path(root, path1, n1) or not self.bottom_up_find_path(root, path2, n2):
            return None

        i, j = len(path1) - 1, len(path2) - 1
        while (i >= 0 and j >= 0):
            if path1[i] != path2[j]: break
            i, j = i-1, j-1

        return path1[i + 1]

class Solution1(object):
    """
    Bottom up recursive dfs approach. Returning the value of the two child nodes.
    Which ever first ancestor node is found with both return values is the LCA.

    Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.LCA(root, p, q)

    def LCA(self, root, p, q):
        if not root or p == root or q == root:  # base cases
            return root

        left_lca = self.LCA(root.left, p, q)
        right_lca = self.LCA(root.right, p, q)

        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        else:
            return right_lca
