from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # Check if the root node is None, if so, return True (an empty tree is complete)
        if not root: return True

        # Create a deque to store the nodes of the tree in level order
        queue = deque([root])

        # Traverse the tree in level order
        while queue[0] is not None:
            # Remove the first node from the deque
            node = queue.popleft()
            # Add the left and right child nodes of the current node to the deque
            queue.append(node.left)
            queue.append(node.right)

        # Remove any remaining None nodes from the beginning of the deque
        while queue and queue[0] is None:
            queue.popleft()

        # Check if there are any remaining nodes in the deque
        # If so, the tree is not complete, so return False
        # Otherwise, the tree is complete, so return True
        return not queue
