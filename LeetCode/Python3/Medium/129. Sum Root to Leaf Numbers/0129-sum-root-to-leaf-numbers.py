# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, r, prev):
        if not r: return 0
        curv = prev * 10 + r.val
        if r.left == None and r.right == None: return curv
        return self.dfs(r.left, curv) + self.dfs(r.right, curv)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)