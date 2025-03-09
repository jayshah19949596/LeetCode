# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        lefts, leafs, rights = [], [], []
        
        def dfs(node, side):
            if side == -1:
                if node.left:
                    lefts.append(node.val)
                    dfs(node.left, side)
                elif node.right:
                    lefts.append(node.val)
                    dfs(node.right, side)
                elif not node.left and not node.right:
                    return
            elif side == 1:
                if node.right:
                    rights.append(node.val)
                    dfs(node.right, side)
                elif node.left:
                    rights.append(node.val)
                    dfs(node.left, side)
                elif not node.left and not node.right:
                    return
            else:
                if not node.left and not node.right:
                    leafs.append(node.val) 
                if node.left: dfs(node.left, side)
                if node.right: dfs(node.right, side)

        if root.left: dfs(root.left, -1)
        if root.right: dfs(root.right, 1)
        dfs(root, 0)

        return [root.val]+lefts+leafs+rights[::-1]
