from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node: TreeNode, currentSum: int = 0, totalPaths: int = 0) -> int:
            if node is None:
                return totalPaths
            currentSum += node.val
            if currentSum == targetSum:
                totalPaths += 1
            totalPaths = traverse(node.left, currentSum, totalPaths)
            totalPaths = traverse(node.right, currentSum, totalPaths)
            return totalPaths
        if root is not None:
            return traverse(root) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return 0
