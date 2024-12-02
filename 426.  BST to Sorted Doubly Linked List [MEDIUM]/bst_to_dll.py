"""
426. BST to Sorted Doubly Linked List [MEDIUM]
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
        self.right = right


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



"""
ITERATIVE
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # base case: when there is nothing, we return NULL
        if root is None: return None
        
        # create a dummy_list for keep track of head, iter_node will traverse the tree in-order dfs fashion and link to build a doubly linked list
        dummy_head = prev = Node(0)
        
        # iterative In-order DFS
        current, stack = root, []
    
        while stack or current:
            while current:
                stack.append(current)
                current = current.left 
            
            # at the first time, this will be the smallest number
            current = stack.pop()
            
            # no need to create a new node, just traverse and connect both ways directly
            prev.right = current
            current.left = prev
            prev = prev.right
    
            current = current.right
    
        # here, at this point, iter_node is the "last node"
        first_node = dummy_head.right
        first_node.left = prev
        prev.right = first_node
        
        # return the first node as requested by prompt
        return dummy_head.right
    
    # TC: O(n) since we visit all nodes in-order dfs.
    # SC: O(n) since we stack to store all values.
