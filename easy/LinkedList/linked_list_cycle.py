# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        # Nodes that have already been checked are flagged.
        checked_flg = 10 ** 6
        tmp = head
        while tmp.next != None:
            if tmp.val == checked_flg:
                return True
            else:
                tmp.val = checked_flg
            tmp = tmp.next

        return False
