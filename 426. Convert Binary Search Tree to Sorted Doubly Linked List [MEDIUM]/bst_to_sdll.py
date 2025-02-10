"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None

        dummy_head = prev = Node(0)
        stack, current = [], root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()

            prev.right = current
            current.left = prev
            prev = prev.right
            
            current = current.right

        # here, at this point, iter_node is the "last node"
        first_node = dummy_head.right
        first_node.left = prev
        prev.right = first_node

        return dummy_head.right
