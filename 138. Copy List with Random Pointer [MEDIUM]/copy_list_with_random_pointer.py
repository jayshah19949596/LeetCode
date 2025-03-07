"""
https://leetcode.com/problems/copy-list-with-random-pointer/

### 1. Question Explanation:
----------------------------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.weaving_in_order_and_unweaving(head)
        # return self.iterative_with_dictionary(head)

    def iterative_with_dictionary(self, head):
        """
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        if not head: return

        visited = {}
        cur_node, copy_prev = head, None
        while cur_node:
            copy_node = Node(cur_node.val)
            if copy_prev: copy_prev.next = copy_node
            visited[cur_node] = copy_node
            copy_prev = copy_node
            cur_node = cur_node.next

        cur_node = head
        while cur_node:
            if cur_node.random:
                copy_node = visited[cur_node]
                copy_node.random = visited[cur_node.random]
            cur_node = cur_node.next
        return visited[head]

    
    def weaving_in_order_and_unweaving(self, head):
        """
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        if not head: return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
