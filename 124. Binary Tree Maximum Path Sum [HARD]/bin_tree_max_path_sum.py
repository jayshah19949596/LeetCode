# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.current_max = float('-inf')
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumHelper(root)
        return self.current_max

    def maxPathSumHelper(self, root):
        """Helper method"""
        if not root:
            return 0
        
        left = self.maxPathSumHelper(root.left)
        right = self.maxPathSumHelper(root.right)
        
        left = max(left, 0)    # do not consider negative child values (set it to zero)
        right = max(right, 0)  # do not consider negative child values (set it to zero)
            
        self.current_max = max(left+right+root.val, self.current_max)
        return max(left, right) + root.val  # return its maximum child plus its own value
