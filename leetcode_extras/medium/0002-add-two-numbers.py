# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Input: 
        l1 = [9,9,9,9,9,9,9], 
        l2 = [9,9,9,9]
             [8,9,9,9,0,0,0,1]
             [8,7,6,5,5,5,5,6,7,8,9]
        '''
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            l1 = ListNode()
        elif l2 is None:
            l2 = ListNode()

        val = l1.val + l2.val

        if val > 9:
            if l1.next is not None:
                l1.next.val += 1
            else:
                l1.next = ListNode(1)
            val = val % 10

        return ListNode(val, next=self.addTwoNumbers(l1.next, l2.next))
