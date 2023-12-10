"""
https://leetcode.com/problems/binary-tree-right-side-view

### 1. Question Explanation:
----------------------------
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.iterative_breadth_first_search(root)
        # return self.iterative_depth_first_search(root)

    def iterative_breadth_first_search(self, root):
        """
        Approach: Level order traversal.
        Traverse nodes from left to right at each level at a time.
        Always add the right most node in the current level being traversed to results array.
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        if not root: return []
        results = []
        current_level = [root]
        while current_level:
            next_level = []
            results.append(current_level[-1].val)
            for node in current_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            current_level = next_level
        return results

    def iterative_depth_first_search(self, root):
        """
        Approach: Depth First Search in post order fashion
        Idea is to keep track of the level.
        For unseen level the  rightmost node will always be first to traverse in post order. Append it to results array.
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        if not root: return []
        results, level_seen = [], set()
        stack = [[root, 0]]
        while stack:
            cur_node, cur_level = stack.pop()
            if cur_level not in level_seen:
                results.append(cur_node.val)
                level_seen.add(cur_level)
            if cur_node.left: stack.append([cur_node.left, cur_level+1])
            if cur_node.right: stack.append([cur_node.right, cur_level+1])
        return results