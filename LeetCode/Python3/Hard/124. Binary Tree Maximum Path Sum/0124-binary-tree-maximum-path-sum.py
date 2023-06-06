# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def max_path(node):
            if not node:
                return 0
            t1 = max(max_path(node.left), 0)
            t2 = max(max_path(node.right), 0)
            res[0] = max(res[0], node.val + t1 + t2)
            return max(t1, t2) + node.val

        max_path(root)
        return res[0]