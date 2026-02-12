class Solution:
    def get_val(self, node):
        if node: return node.val
        return 0

    def reverse_list(self, head):
        prv_node, node = head, head.next
        prv_node.next = None
        while node: 
            nxt_node = node.next
            node.next = prv_node
            prv_node = node
            node = nxt_node
        return prv_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        node = dummy = ListNode(-1)
        while l1 or l2 or carry:
            val1, val2 = self.get_val(l1), self.get_val(l2)
            total = val1+val2+carry
            carry = total//10
            nxt_val = total%10
            node.next = ListNode(nxt_val)
            node = node.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return self.reverse_list(dummy.next)
