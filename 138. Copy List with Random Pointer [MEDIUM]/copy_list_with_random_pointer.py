"""
https://leetcode.com/problems/copy-list-with-random-pointer/

### 1. Question Explanation:
----------------------------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

### 3. Complexity Analysis:
----------------------------
Time Complexity - O(N)
Space Complexity - O(N)
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        visited = {}
        node, copy_prev = head, None
        while node:
            copy_node = Node(node.val)
            if copy_prev: copy_prev.next = copy_node
            visited[node] = copy_node
            copy_prev = copy_node
            node = node.next

        node, copy_node = head, visited[head]
        while copy_node:
            if node.random:
                copy_node.random = visited[node.random]
            copy_node = copy_node.next
            node = node.next

        return visited[head]