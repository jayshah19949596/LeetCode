# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<2 : return head
        
        node = head
        for _ in range(k):
            if not node: return head
            node = node.next
            
        prev_node = self.reverseKGroup(node, k)
        curr_node = head
        for _ in range(k):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node
