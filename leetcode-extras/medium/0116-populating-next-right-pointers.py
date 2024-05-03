"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
          1
        2   3

            1
          2   3
        4  5 6  7
        '''
        if root is None:
            return

        queue = [root]

        i = 0
        h = 0
        while queue:
            node = queue.pop(0)
            i += 1
            l, r = node.left, node.right
            if l and r:
                queue.append(l)
                queue.append(r)

            if queue:
                node.next = queue[0]

            if i == 2**h:
                print(node.val, h)
                i = 0
                h += 1
                node.next = None

        return root
