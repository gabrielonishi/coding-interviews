# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reverse_head = node = self.reverseList(head.next)

        while node.next:
            node = node.next
        
        node.next = ListNode(val = head.val)

        return reverse_head
