"""
### 1. Solution Explanation:
----------------------------
Using priority queue to insert elements and pop and create Linked List Nodes.

###  Complexity Analysis:
----------------------------
Time complexity : O(N*Logk)
Space Complexity: O(N)
"""

from typing import List, Optional
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = dummy = ListNode(0)
        queue = []

        for i, l in enumerate(lists):
            if not l: continue
            heappush(queue, (l.val, i, l))
            i += 1

        while queue:
            val, _, node = heappop(queue)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if node.next:
                node = node.next
                heappush(queue, (node.val, i, node))
                i += 1

        return head.next