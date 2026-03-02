# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 1) Find prevA (node at index a-1)
        prevA = list1
        for _ in range(a - 1):
            prevA = prevA.next

        # 2) Find afterB (node at index b+1)
        cur = prevA
        for _ in range(b - a + 2):   # move from (a-1) to (b+1)
            cur = cur.next
        afterB = cur

        # 3) Connect prevA -> list2
        prevA.next = list2

        # 4) Find tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # 5) Connect tail2 -> afterB
        tail2.next = afterB

        return list1
