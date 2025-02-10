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
        if not root: return
        # The smallest (first) and the largest (last) nodes
        first, last = None, None

        def dfs_inorder_helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            if not node: return

            dfs_inorder_helper(node.left)  # left

            nonlocal last, first
            # if last and node: print("last", last.val, "node", node.val)
            if last:
                # link the previous node (last) with the current one (node)
                last.right = node
                node.left = last
            else:
                first = node # keep the smallest node to close DLL later on
            last = node

            dfs_inorder_helper(node.right)  # right

        dfs_inorder_helper(root)

        # close DLL
        last.right = first
        first.left = last
        return first


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
