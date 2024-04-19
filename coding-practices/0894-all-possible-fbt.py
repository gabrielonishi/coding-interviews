# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {0: [], 1: [TreeNode()]}

        def recurse(n: int) -> List[TreeNode]:
            if n in memo:
                return memo[n]

            res = []

            for l in range(n):
                r = n - l - 1
                leftTrees = recurse(l)
                rightTrees = recurse(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))

            memo[n] = res

            return res

        return recurse(n)
