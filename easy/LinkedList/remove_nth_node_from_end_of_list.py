# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        # Find the size of the linked list
        tmp = head
        size = 0
        while tmp:
            size += 1
            tmp = tmp.next

        # In case we have to remove the first node
        if n == size:
            return head.next

        # Delete target node
        tmp = head
        for i in range(size - n - 1):
            tmp = tmp.next
        tmp.next = tmp.next.next

        return head
