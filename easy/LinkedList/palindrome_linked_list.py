# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        # Get values of linked-lists
        store_list = []
        tmp = head
        while tmp.next != None:
            store_list.append(tmp.val)
            tmp = tmp.next
        store_list.append(tmp.val)

        # Reverse the list and compare it to the original list
        ori_list = store_list.copy()
        store_list.reverse()
        if ori_list == store_list:
            return True

        return False
