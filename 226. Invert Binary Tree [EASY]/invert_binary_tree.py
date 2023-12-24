from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return self.iterative_bfs(root)
        return self.recurse_dfs(root)

    def iterative_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        APPROACH 1: ITERATIVE BFS
        """
        if not root: return None
        queue = deque([root])

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

        return root

    def recurse_dfs(self, node):
        """
        APPROACH 2: RECURSIVE DFS
        """
        if not node: return None

        left_node = self.recurse_dfs(node.left)
        right_node = self.recurse_dfs(node.right)

        node.right, node.left = left_node, right_node
        return node
