from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_arr = []
        i = 0
        for l_node in lists:
            if not l_node: continue
            heappush(heap_arr, (l_node.val, i, l_node))
            i += 1

        head = dummy = ListNode()
        while heap_arr:
            val, _, node = heappop(heap_arr)
            dummy.next = node
            dummy = dummy.next
            if node.next: 
                heappush(heap_arr, (node.next.val, i, node.next))
                i += 1
        
        return head.next
