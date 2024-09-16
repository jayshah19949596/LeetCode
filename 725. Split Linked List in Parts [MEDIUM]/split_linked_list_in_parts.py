# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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