# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Return None in case empty pattern
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        # Get values from list1
        num_list = []
        tmp = list1
        while tmp.next != None:
            num_list.append(tmp.val)
            tmp = tmp.next
        num_list.append(tmp.val)

        # Get values from list2
        tmp = list2
        while tmp.next != None:
            num_list.append(tmp.val)
            tmp = tmp.next
        num_list.append(tmp.val)

        num_list.sort()
        # Merge list1 and list2
        tmp.next = list1

        # Insert sorted values to merged list
        tmp = list2
        i = 0
        while tmp.next != None:
            tmp.val = num_list[i]
            tmp = tmp.next
            i += 1
        tmp.val = num_list[i]

        return list2
