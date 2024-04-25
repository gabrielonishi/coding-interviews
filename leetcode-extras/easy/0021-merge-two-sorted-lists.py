# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next

        head_storage = {0: head}

        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next

        if list1 is None and list2:
            head.next = list2
            return head_storage[0]

        if list2 is None and list1:
            head.next = list1
            return head_storage[0]

        return head_storage[0]
