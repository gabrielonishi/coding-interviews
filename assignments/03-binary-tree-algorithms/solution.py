from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return (self.traverse(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))

    def traverse(self, node: TreeNode, targetSum: int, current_sum: int = 0) -> int:
        if not node:
            return 0

        current_sum += node.val
        count = 0
        if current_sum == targetSum:
            count += 1

        count += self.traverse(node.left, targetSum, current_sum)
        count += self.traverse(node.right, targetSum, current_sum)

        return count
