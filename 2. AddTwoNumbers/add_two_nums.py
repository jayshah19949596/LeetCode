"""
=========================
APPROACH 1: Merging two linked list in one linkedin list by math.
Traverse each two linked list at same time.
for each node of the two linkedin list add them and create a new node of the resulting linkedin list 

Time - O(max(len(l1), len(l2)))
Space - O(max(len(l1), len(l2)))
=========================
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        node = dummy = ListNode(-1)
        
        def get_val(node):
            if node: return node.val
            return 0
            
        while l1 or l2 or carry:
            val1, val2 = get_val(l1), get_val(l2)
            total = val1+val2+carry
            carry = total//10
            nxt_val = total%10
            node.next = ListNode(nxt_val)
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
