"""
206. Reverse Linked List [EASY]
https://leetcode.com/problems/reverse-linked-list


### 1. Question:
----------------------------
Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, curr_node = None, head

        while curr_node:
            next_node = cur_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node
