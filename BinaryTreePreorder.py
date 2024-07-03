# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion version
    def preorderTraversalRecursion(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = [root.val]

        if root.left is None and root.right is None:
            return result
        if root.left is not None:
            result.extend(self.preorderTraversal(root.left))
        if root.right is not None:
            result.extend(self.preorderTraversal(root.right))
        return result

