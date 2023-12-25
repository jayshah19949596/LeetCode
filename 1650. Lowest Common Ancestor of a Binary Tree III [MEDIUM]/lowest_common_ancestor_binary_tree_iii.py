"""
1650. Lowest Common Ancestor of a Binary Tree III [MEDIUM]

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

### 1. Question Explanation:
----------------------------
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# APPROACH 1: Parent Path
class Solution:
    """
    The idea is to store the parents (path) from root to p, and then check q's path.
    First q's parent found in p's parent path is the LCA.

    Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q


# APPROACH 2: Finding the convergence
class Solution:
    """
    The idea is the same as finding the convergence point of 2 linked lists.
    We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively.
    Then we follow their parent pointers until they point to the same node.
    When either of the pointers points to root, we set it to the other original starting node.
    For example, when p1 points to root (i.e p1.parent is None), assign q to p1.

    Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        current_p, current_q = p, q
        while current_p != current_q:
            if current_p: current_p = current_p.parent
            else: current_p = q
            if current_q: current_q = current_q.parent
            else: current_q = p
        return current_p
