"""
235. Lowest Common Ancestor of a Binary Search Tree [MEDIUM]
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

### 1. Question:
----------------------------
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
-------------------------------------------------------------------------
Approach 1: Bottom-up recustion without Pruning with Binary Search Tree 
-------------------------------------------------------------------------
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node: return None
            if node == p or node == q:
                return node
            left_ans = dfs(node.left, p, q)
            right_ans = dfs(node.right, p, q)

            if left_ans and right_ans:
                return node
            elif left_ans:
                return left_ans
            elif right_ans:
                return right_ans
            else:
                return None

        return dfs(root, p, q)


"""
---------------------------------------------------------------------
Approach 2: Bottom-up recustion WITH Pruning [SUB-Optimal Pruning]
---------------------------------------------------------------------
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if not node: return 
            if node == p or node == q: return node 
            
            left_return =  right_return = None
            if p.val<node.val or q.val<node.val:
                left_return = dfs(node.left, p, q)
            if p.val>node.val or q.val>node.val:
                right_return = dfs(node.right, p, q)
            
            if left_return and right_return: 
                return node  
            elif left_return: 
                return left_return
            elif right_return: 
                return right_return
        return dfs(root, p, q)

"""
---------------------------------------------------------------------
Approach 3: Top-down recustion WITH top level Pruning ONLY [MOST-Optimal Pruning]
---------------------------------------------------------------------
"""
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
