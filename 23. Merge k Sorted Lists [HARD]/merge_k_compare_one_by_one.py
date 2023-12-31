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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        node = head = None
        end_of_list_count = 0

        while end_of_list_count != k:
            min_klist_idx, min_val = -1, float('inf')
            end_of_list_count = 0

            for i, klist in enumerate(lists):
                if klist and klist.val < min_val:
                    min_val = klist.val
                    min_klist_idx = i
                if klist is None:
                    end_of_list_count += 1

            if min_klist_idx != -1:
                new_node = ListNode(min_val, None)
                if not node:
                    head = node = new_node
                else:
                    node.next = new_node
                    node = node.next
                lists[min_klist_idx] = lists[min_klist_idx].next

        return head
