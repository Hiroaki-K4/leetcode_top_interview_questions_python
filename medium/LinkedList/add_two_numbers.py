# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Get l1 number
        l1_num = 0
        digit = 1
        while l1:
            l1_num += digit * l1.val
            digit *= 10
            l1 = l1.next

        # Get l2 number
        l2_num = 0
        digit = 1
        while l2:
            l2_num += digit * l2.val
            digit *= 10
            l2 = l2.next

        # Create answer by using l1 and l2 numbers
        ans_num = l1_num + l2_num
        first_val = ans_num % 10
        ans_num //= 10
        ans_node = ListNode(val=first_val)
        tmp_node = ans_node
        while ans_num > 0:
            new_val = ans_num % 10
            new_node = ListNode(val=new_val)
            tmp_node.next = new_node
            ans_num //= 10
            tmp_node = tmp_node.next

        return ans_node
