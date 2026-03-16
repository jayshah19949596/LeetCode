"""
Approach:

We reverse the linked list only between positions left and right in one pass.

First, we use a dummy node pointing to the head to simplify edge cases (for example when left = 1). Then we move a pointer prev to the node just before the reversal starts.

Next, we start reversing nodes between left and right using the head insertion technique. We keep the first node of the sublist fixed and repeatedly move the next node to the front of the reversed portion. This gradually builds the reversed section in place while maintaining connections with the rest of the list.

Finally, we return dummy.next, which points to the new head of the modified list.

"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_node = dummy

        # move prev to node before reversal and always remains this node
        for _ in range(left - 1):
            prev_node = prev_node.next

        # cur points to at reversal and always remains this node
        curr_node = prev_node.next

        """
        Reverse nodes between left and right
        prev always remains the same. curr always remains the same.
        temp is the target that get's shifte to the front. 
        Each iteration takes the node pointed to by temp and inserts it right after prev.
        """ 
        for _ in range(right - left):
            temp_node = curr_node.next
            curr_node.next = temp_node.next
            temp_node.next = prev_node.next
            prev_node.next = temp_node

        return dummy.next
