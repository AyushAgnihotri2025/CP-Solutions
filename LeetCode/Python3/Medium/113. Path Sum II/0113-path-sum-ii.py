# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(path,r):
            if r:
                if not r.left and not r.right:
                    path.append(r.val)
                    if sum(path)==targetSum:
                        res.append(path)
                dfs(path+[r.val],r.left)
                dfs(path+[r.val],r.right)
        dfs([],root)
        return res