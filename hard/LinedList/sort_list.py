# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one element
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None  # Split the list into two parts

        # Sort each half recursively
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def getMiddle(self, head: ListNode) -> ListNode:
        # Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Merge two sorted linked lists
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append any remaining nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next
