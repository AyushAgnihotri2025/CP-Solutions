# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, result):
            if not node:
                return [-1, -1]
            left, right = dfs(node.left, result), dfs(node.right, result)
            result[0] = max(result[0], left[1]+1, right[0]+1)
            return [left[1]+1, right[0]+1]

        result = [0]
        dfs(root, result)
        return result[0]