# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.cur = None
        
        def dfs(node):
            if not node:
                return
            left, right = node.left, node.right
            node.left = None
            if self.cur:
                self.cur.right = node
                self.cur = self.cur.right
            else:
                self.cur = node
            dfs(left)
            dfs(right)

        dfs(root)