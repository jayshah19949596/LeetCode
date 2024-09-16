"""
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False


    def next(self):
        """
        :rtype: int
        """
        return_node = self.stack.pop()
        if return_node.right:
            node = return_node.right
            while node:
                self.stack.append(node)
                node = node.left
        return return_node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())