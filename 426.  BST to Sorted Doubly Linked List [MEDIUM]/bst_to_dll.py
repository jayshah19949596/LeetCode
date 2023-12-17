"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

### 1. Question Explanation:
----------------------------
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.


### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                helper(node.left)  # left

                # node
                if last:
                    # link the previous node (last) with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node to close DLL later on
                    first = node
                last = node

                helper(node.right)  # right

        if not root:
            return None

        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)

        # close DLL
        last.right = first
        first.left = last
        return first