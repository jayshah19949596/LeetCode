class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        # search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1 & 2: node has 0 or 1 child
            if not root.left: return root.right
            if not root.right: return root.left

            # Case 3: node has two children
            # Find smallest in right subtree
            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val

            # delete successor
            root.right = self.deleteNode(root.right, cur.val)

        return root
