"""
1382. Balance a Binary Search Tree [MEDIUM]
https://leetcode.com/problems/balance-a-binary-search-tree

### 1. Question Explanation:
----------------------------
Given the root of a binary search tree, return a balanced binary search tree with the same node values.
If there is more than one answer, return any of them.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []

        def dfs_inorder_serialize(node):
            nonlocal array
            if node.left: dfs_inorder_serialize(node.left)
            array.append(node.val)
            if node.right: dfs_inorder_serialize(node.right)
        dfs_inorder_serialize(root)

        def rebuild_with_balance(arr, low, high):
            if low<=high:
                mid = (low+high)//2
                left_node = rebuild_with_balance(arr, low, mid-1)
                right_node = rebuild_with_balance(arr, mid+1, high)
                node = TreeNode(arr[mid], left_node, right_node)
                return node
            return None

        return rebuild_with_balance(array, 0, len(array)-1)