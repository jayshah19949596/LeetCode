class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            target_node = Node(insertVal, None)  
            target_node.next = target_node
            return target_node
        cur_node = head
        nxt_node = head.next
        to_insert = False
        while nxt_node != head:
            
            if cur_node.val<=insertVal<=nxt_node.val:
                # Inserting in between low and high
                to_insert = True
            elif cur_node.val>nxt_node.val:
                # Inserting in the tail
                if cur_node.val<=insertVal or insertVal<=nxt_node.val:
                    to_insert = True
            
            if to_insert:
                cur_node.next = Node(insertVal, nxt_node)
                break
            
            cur_node = cur_node.next
            nxt_node = nxt_node.next
        
        else:
            # Inserting in the loop with all same values 
            cur_node.next = Node(insertVal, nxt_node)  

        return head
