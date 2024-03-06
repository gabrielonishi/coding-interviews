'''
Problem 4.6 - Cracking the Coding Interview

Write an algorithm to find the "next" node (i.e., in-order successor) of a given node 
in a binary search tree. You may assume that each node has a link to its parent.

Definitions

    Binary Search Tree: a binary tree for which the following is valid for all nodes: 
    the value in the node is greater than all values on the left sub-tree and less 
    than or equal to all values in the right sub-tree.
'''

class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_father(node: TreeNode, target: int) -> TreeNode:
    if node is None: 
        return None
    elif node.value == target:
        return node
    else:
        return find_father(node.parent, target)

def find_son(node: TreeNode, target: int) -> TreeNode: 
    if node is None:
        return None
    elif node.value == target:
        return node
    elif target > node.value:
        return find_son(node.right, target)
    else:
        return find_son(node.left, target)

def in_order_succ(node: TreeNode) -> TreeNode:
    
    if node is None: return None
    
    target = node.value + 1

    father = find_father(node, target) 
    
    if father is not None:
        return father
    
    return find_son(node, target)