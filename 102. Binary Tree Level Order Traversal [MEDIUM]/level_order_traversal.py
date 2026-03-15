# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level = [root]
        results = []
      
        while level:
            results.append([])
            nxt_level = []
            for node in level:
                results[len(results)-1].append(node.val)
                if node.left: nxt_level.append(node.left)
                if node.right: nxt_level.append(node.right)
            level = nxt_level
          
        return results
            
