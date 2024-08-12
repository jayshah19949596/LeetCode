"""
=========================
APPROACH 1: Intutive number conversion approach.
Convert content of l1 in number and content of l2 in number. 
Add the two numbers and convert resulting number to a linked list.

Time - O(max(len(l1), len(l2)))
Space - O(max(len(l1), len(l2)))
=========================
"""
class Solution:
    def get_num(self, lnode):
        digits = []
        while lnode:
            digits.append(lnode.val)
            lnode = lnode.next
        num = 0
        for i in range(len(digits)-1, -1, -1):
            num = num*10 + digits[i]
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = self.get_num(l1), self.get_num(l2)
        res_num = num1+num2
        if res_num == 0: return ListNode(0)
        cur_node = dummy = ListNode()
        while res_num != 0:
            remainder = res_num%10
            res_num = res_num//10
            cur_node.next = ListNode(remainder)
            cur_node = cur_node.next
        return dummy.next


"""
=========================
APPROACH 2: Merging two linked list in one linkedin list by math.
Traverse each two linked list at same time.
for each node of the two linkedin list add them and create a new node of the resulting linkedin list 

Time - O(max(len(l1), len(l2)))
Space - O(max(len(l1), len(l2)))
=========================
"""
class Solution:
    def get_value_of_node(self, lnode):
        if lnode is not None:
            return lnode.val
        return 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            val1, val2 = self.get_value_of_node(l1), self.get_value_of_node(l2)

            # Calculate the sum of the current digits plus carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next nodes
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
