"""
This solution get TLE

### 1. Solution Explanation:
----------------------------
1. Compare every k nodes (head of every linked list) and get the node with the smallest value.
2. Extend the final sorted linked list with the selected nodes.

###  Complexity Analysis:
----------------------------
Time complexity : O(k*N)
Space Complexity: O(N)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, klists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur_node = ListNode(0)
        while True:
            min_node, min_idx = ListNode(float("inf")), None
            for i, node in enumerate(klists):
                if node and min_node.val>node.val:
                    min_node, min_idx = node, i
            if min_idx is None: break
            klists[min_idx] = klists[min_idx].next
            cur_node.next = min_node
            cur_node = cur_node.next
        return dummy.next
