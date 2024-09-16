"""
725. Split Linked List in Parts [MEDIUM]
https://leetcode.com/problems/split-linked-list-in-parts/

### 1. Question Explanation:
----------------------------
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.

### 2. Solution Explanation:
----------------------------
We are given a linked list head and an integer k.
We want to split head evenly into k equally sized parts and return an array of the k parts.
If head cannot be split evenly, the sizes of the k parts can differ by at most 1, with the larger parts appearing before the smaller ones.



### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k
        size, current = 0, head
        while current:
            size += 1
            current = current.next

        split_size = size // k
        num_remaining_parts = size % k
        current = head

        for i in range(k):
            new_node = new_head = ListNode(0)
            current_size = split_size
            if num_remaining_parts > 0:
                num_remaining_parts -= 1
                current_size += 1
            for j in range(current_size):
                new_node.next = ListNode(current.val)
                new_node = new_node.next
                current = current.next
            ans[i] = new_head.next

        return ans