'''
Problem 2.7 - Cracking the Coding Interview

Given two linked lists, determine if the two lists intersect. Return the intersection node.
Definitions

    Intersection: the intersection of two linked lists is based on reference, not value. In other words, even if two lists have nodes with the same value, that doesn't mean they intersect.

Additional information

    The lists are singly linked, i.e. there is no pointer to the previous node.

Hints

     - Examples are useful. Draw two linked lists with an intersection and two equivalent lists that don't intersect;
     - Start by checking if there is an intersection before looking for the exact place it occurs;
     - Note that if two lists intersect, they will always share the last node. Once they intersect, all following nodes are shared;
     - After you have determined that the two lists intersect, you have to find the intersection node. If the two lists had the exact same length, how would you solve the problem?
     - If the two lists had the same length, you could traverse them in parallel until you find a shared node. Now, how can you adapt this idea to lists with different lengths?
     - Is the length difference useful for anything?

'''

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt    

def find_intersection(head1: Node, head2: Node) -> Node:

    if head1 is None or head2 is None:
        return None

    size1 = 1    
    tail1 = head1
    
    size2 = 1
    tail2 = head2
    
    while tail1.next is not None:
        tail1 = tail1.next
        size1 += 1
    
    while tail2.next is not None:
        tail2 = tail2.next
        size2 += 1
        
    if tail1 != tail2:
        return None

    size_diff = size1 - size2
    
    node1 = head1
    node2 = head2
    
    for i in range(abs(size_diff)):
        if size_diff > 0:
            node1 = node1.next
        else:
            node2 = node2.next
    
    while node1 is not None or node2 is not None:
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next
    
    return None