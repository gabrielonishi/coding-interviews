# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return

        ll_list = list()
        
        while head:
            ll_list.append(head)
            head = head.next
        
        new_head = ret = ListNode(ll_list[-1].val)

        for i in range(len(ll_list) - 2, -1, -1):
            new_head.next = ListNode(ll_list[i].val)
            new_head = new_head.next

        return ret
