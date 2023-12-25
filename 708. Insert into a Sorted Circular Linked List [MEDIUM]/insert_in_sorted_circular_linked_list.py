"""
708. Insert into a Sorted Circular Linked List [MEDIUM]

https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

### 1. Question Explanation:
----------------------------
Given a Circular Linked List node, which is sorted in non-descending order.
Write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

#### Example 1:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.

#### Example 2:
Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

#### Example 3:
Input: head = [1], insertVal = 0
Output: [1,0]

### 2. Complexity Analysis

Time Complexity: O(N)

Space Complexity: O(1)
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insert_val: int) -> 'Node':

        if head == None:
            newNode = Node(insert_val, None)
            newNode.next = newNode
            return newNode

        prev, curr = head, head.next
        to_insert = False

        while curr != head:

            if prev.val <= insert_val <= curr.val:
                # Case-1: The value of new node sits between the minimal and maximal values of the current list
                to_insert = True
            elif prev.val > curr.val:
                # Case-2. where we locate the tail element 'prev' points to the tail, i.e. the largest element!
                if insert_val >= prev.val or insert_val <= curr.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insert_val, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next

        # Case-3: There is one case that does not fall into any of the above two cases i.e. did not insert the node in the loop.
        # This is the case where the list contains uniform values.
        prev.next = Node(insert_val, curr)
        return head