"""
====================================
Solution 1: Iterative
====================================
"""
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next


"""
====================================
Solution 2: Recursive bottom-up
====================================
"""
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2

        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
  
