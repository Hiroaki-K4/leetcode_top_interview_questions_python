# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Add the head of each linked list to the heap
        for i, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # Get the smallest node from the heap
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next

            # If there's a next node, add it to the heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
