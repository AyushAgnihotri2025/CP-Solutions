# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        def sum(node,s,S):
            if node.left is None and node.right is None:
                S.append(s)
            if node.left is not None:
                sum(node.left,s+node.left.val,S)
            if node.right is not None:
                sum(node.right,s+node.right.val,S)
            return S
        return targetSum in sum(root,root.val,[])