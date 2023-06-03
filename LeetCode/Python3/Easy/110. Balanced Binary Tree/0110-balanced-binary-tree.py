# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        def compareH(node):
            if node is None:
                return 1
            dr = compareH(node.right)
            if dr == 0:
                return 0
            dl = compareH(node.left)
            if dl == 0:
                return 0
            if abs(dr-dl) > 1:
                return 0
            return max(dr,dl)+1

        return compareH(root) != 0