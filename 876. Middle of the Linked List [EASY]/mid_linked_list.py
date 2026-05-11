# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = head
        i = 0
        while q: 
            q = q.next
            i += 1
            if i%2 == 0: p = p.next
        return p
