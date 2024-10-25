# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, both start at the dummy node
        first = dummy
        second = dummy

        # Move first pointer n steps ahead
        for _ in range(n):
            first = first.next

        # Move both first and second until first reaches the end of the list
        while first.next:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Return the head of the updated list
        return dummy.next
