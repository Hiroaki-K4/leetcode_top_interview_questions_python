# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # Get all vals
        vals = []
        tmp = head
        while tmp.next != None:
            vals.append(tmp.val)
            tmp = tmp.next
        vals.append(tmp.val)

        # Reverse vals
        vals.reverse()

        # Reverse vals of linked-list
        tmp = head
        i = 0
        while tmp.next != None:
            tmp.val = vals[i]
            tmp = tmp.next
            i += 1
        tmp.val = vals[i]

        return head
