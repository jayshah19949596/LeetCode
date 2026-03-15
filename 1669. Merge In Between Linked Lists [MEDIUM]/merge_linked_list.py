# Definition for singly-linked list.
# class ListNode:a
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node, i = list1, 0        
        while i <= b:
            if i == a-1: 
                prev_a_node = node
            if i == b: 
                b_node = node
            node = node.next
            i += 1
        
        prev_a_node.next = node = list2
        while node.next: 
            node = node.next
        node.next = b_node.next
        return list1
